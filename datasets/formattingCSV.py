"""
CSV Formatter for NI2024-Stranieri_altri_dati_2.csv 
==================================

Output Format:
-------------
The script produces a CSV file with the following columns:
- Year: The year of the data point
- Age_Group: Age range or 'Total'
- Education_Level: Type of education qualification
- Foreign_Percentage: Percentage for foreign population
- Italian_Percentage: Percentage for Italian population

"""

import pandas as pd
import numpy as np

def clean_raw_data(raw_text):
    lines = [line.strip() for line in raw_text.split('\n')]
    lines = [line for line in lines if line and not line.startswith('Fonte:')]
    return lines

def identify_sections(lines):
    sections = {}
    for i, line in enumerate(lines):
        if 'LICENZA MEDIA' in line:
            sections['Licenza_Media'] = i
        elif 'DIPLOMA' in line:
            sections['Diploma'] = i
        elif 'TITOLO UNIVERSITARIO' in line:
            sections['Titolo_Universitario'] = i
    return sections

def parse_data_line(line):
    parts = [p.strip() for p in line.split(';') if p.strip()]
    if len(parts) == 0:
        raise ValueError(f"Line parsing error: {line}")
    year = parts[0].strip()
    values = [float(v.replace(',', '.')) for v in parts[1:] if v and v != ' ']
    return year, values

def process_section(lines, start_idx, end_idx):
    data_rows = []
    age_groups = ['15-24', '25-34', '35-44', '45-54', '55-64', 'Total']
    
    current_line = start_idx + 1
    while current_line < end_idx:
        line = lines[current_line]
        if line and not line.startswith('ANNI') and ';' in line:
            try:
                year, values = parse_data_line(line)
                if year.strip() and year.strip().isdigit():
                    for i in range(0, len(values), 2):
                        if i//2 < len(age_groups):
                            data_rows.append({
                                'year': int(year),
                                'age_group': age_groups[i//2],
                                'foreign_percentage': values[i],
                                'italian_percentage': values[i+1]
                            })
            except ValueError as e:
                print(f"Error processing line {current_line}: {e}")
        current_line += 1
    return data_rows

def format_education_data(raw_text):
    lines = clean_raw_data(raw_text)
    sections = identify_sections(lines)
    section_list = sorted(sections.items(), key=lambda x: x[1])
    
    all_data = []
    for i in range(len(section_list)):
        start_idx = section_list[i][1]
        end_idx = section_list[i+1][1] if i < len(section_list)-1 else len(lines)
        section_data = process_section(lines, start_idx, end_idx)
        
        for row in section_data:
            row['education_level'] = section_list[i][0]
        
        all_data.extend(section_data)
    
    df = pd.DataFrame(all_data)
    df = df.sort_values(['year', 'education_level', 'age_group'])
    df = df[['year', 'age_group', 'education_level', 
             'foreign_percentage', 'italian_percentage']]
    df.columns = ['Year', 'Age_Group', 'Education_Level', 
                 'Foreign_Percentage', 'Italian_Percentage']
    
    return df

def save_formatted_data(df, output_file):
    df.to_csv(output_file, index=False)
    print(f"Data saved to {output_file}")

def main():
   # Input the path to YOUR OWN input and output CSV files here
    input_file = '/path/to/your/input_file.csv'  # Replace with the actual path to your input CSV file
    output_file = '/path/to/your/output_file.csv'  # Replace with the actual path to your output CSV file
    
    # Debugging: Print the file paths to ensure they are correct
    print(f"Reading input file: {input_file}")
    print(f"Output file will be saved to: {output_file}")
    
    # Read input file
    with open(input_file, 'r', encoding='utf-8') as f:
        raw_text = f.read()
    
    # Format data
    print("Formatting data...")
    formatted_df = format_education_data(raw_text)
    
    # Save formatted data
    print("Saving formatted data...")
    save_formatted_data(formatted_df, output_file)
    print("Data saved successfully.")

# Example usage
if __name__ == "__main__":
    main()