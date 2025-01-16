import pandas as pd


def calculate_completeness_pandas(dataframe):
    # Total number of cells in the dataset
    total_values = dataframe.size

    # count null values, including specific indicators of missing values (' ', '', '-', '.')
    null_values = (
        dataframe.isin([" ", "", "-", "."]).sum().sum() + dataframe.isnull().sum().sum()
    )

    # calculate completeness percentage
    completeness_percentage = ((total_values - null_values) / total_values) * 100

    return {
        "total_values": total_values,
        "null_values": null_values,
        "completeness_percentage": round(completeness_percentage, 2),
    }


# load the dataset using the absolute path from YOUR local file system
dataset = pd.read_csv("/path/to/dataset.csv")

completeness_results = calculate_completeness_pandas(dataset)
print(completeness_results)
