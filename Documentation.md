# Table of Contents

1.  **[Introduction](#introduction)**
    
2.  **[Scenario](#scenario)**
    
3.  **[Original Dataset and Mashed-up Dataset](#datasets)**  
    3.1 [Original Datasets](#s-3-1)  
    3.2 [Mashed-up Datasets](#s-3-2) 
        
4.  **[Quality Analysis of the Datasets](#quality-analysis)**
    
5.  **[Legal Analysis](#legal-analysis)**  
    
6.  **[Ethics Analysis](#ethics-analysis)**  
    
7.  **[Technical Analysis](#technical-analysis)**  
    
8.  **[Sustainability of Dataset Updates Over Time](#sustainability)**  
    
9.  **[Visualization](#visualization)**  
    _(To be filled with content)_
    
10.  **[RDF Assertion of Metadata](#rdf)**  
    
11.  **[Conclusions](#conclusions)**

# 1.	Introduction <a name="introduction"></a>

In recent years, Italy has experienced a significant increase in immigration, impacting various sectors of society. [According to a 2024 report by La Repubblica](https://www.repubblica.it/cronaca/2024/02/13/news/immigrati_record_di_assunzioni_nel_2023_piu_stranieri_residenti_regolari_effetto_della_sanatoria_del_2020-422119125), the foreign resident population in Italy has grown notably, with a significant rise in the number of regular foreign workers. Additionally, [the number of foreign entrepreneurs has been on the rise](https://finanza.repubblica.it/News/2024/10/15/lavoro_da%C2%A0immigrati_l8_8_percento_del_pil_italiano_punte_in_agricoltura_16_4percento_e_costruzioni_15_1percento_-147/), with 776,000 immigrant entrepreneurs recorded in 2023, accounting for 10.4% of the total. 
 
This demographic shift underscores the importance of understanding migration patterns and their implications. In response, DeMi (Decoding Migration) has been carried out for the exam "Open Access and Digital Ethics" as a part of the [Digital Humanities and Digital Knowledge course](https://corsi.unibo.it/2cycle/DigitalHumanitiesKnowledge) at the University of Bologna. The two contributors to DeMi are:
* Ekaterina Krasnova,
*	Mohammad Javad Farokhi Darani.

DeMi aims to study and analyze migration trends and demographics in Italy, focusing on two primary research questions:
* What are the main countries of origin of immigrants in Italy, and how have these trends evolved over the last five years?
* What are the demographic profiles of immigrants in Italy, including age, gender, and education level?

The background of this project stems from the increasing significance of migration as local phenomenon, particularly within Italy. Migration impacts various aspects of society, such as labor markets, education, and public policy. The idea behind DeMi is to harness open datasets and digital tools to analyze migration trends, offering insights that enhance understanding of migration dynamics and guide policymaking.

To achieve its objectives, DeMi utilizes a collection of open datasets that have been analyzed from legal, ethical, and technical perspectives. The datasets were processed to create mashed-up data compliant with the principles of Linked Open Data, incorporating RDF models aligned with the [DCAT-AP](https://www.w3.org/TR/vocab-dcat-3/) ontology. This approach enabled the generation of high-quality, [5-star Linked Open Data](https://www.w3.org/community/webize/2014/01/17/what-is-5-star-linked-data/), which is freely downloadable and reusable.

The results of this project are presented through an interactive and user-friendly website, supported by documentation. Additionally, all scripts and derived datasets are shared on the project's GitHub repository under an open license, ensuring that the research is transparent, repeatable, and accessible to a broad audience.

# 2.	Scenario <a name="scenario"></a>

DeMi seeks to provide valuable insights into the trends and profiles of immigrants in Italy, helping to address knowledge gaps and promote informed decision-making. By examining the main countries of origin of immigrants, along with their demographic profiles, our research aims to highlight patterns that are often underrepresented or misunderstood.

The information provided by DeMi holds immense value for a diverse range of individuals and groups. Researchers can use our findings to deepen their understanding of migration trends, uncovering patterns that inform studies on demographics, education, and labor markets. Policymakers, in turn, can rely on this data to craft targeted strategies for social integration, allocate resources more effectively, and design initiatives that address the needs of immigrant populations. Educators may find the demographic and educational insights particularly useful for shaping curricula and support programs that cater to students from diverse cultural and educational backgrounds. Similarly, community leaders and advocacy groups can leverage the data to develop initiatives like language workshops or mentorship programs, ensuring immigrants have the tools they need to integrate. Journalists and activists can use our research to challenge stereotypes and foster a more nuanced understanding of migration in public discourse.

However, despite its broad utility, the project encountered significant challenges. A notable issue was the lack of recent updates in many datasets, with some containing no new data since 2012. This presented difficulties in ensuring that our analysis was as accurate and comprehensive as possible.

Through these efforts, DeMi aims to empower a wide range of stakeholders by providing open, accessible, and reliable data. By presenting migration trends and insights in an understandable and meaningful way, our project contributes to a more informed and empathetic discourse on migration, supporting the development of more inclusive societies.

# 3.	Original dataset and mashed-up dataset <a name="datasets"></a>

### 3.1. Original datasets <a name="s-3-1"></a>
Here there is a description for each of original datasets:

**IstatData**

url: https://esploradati.istat.it/

IstatData is the new platform to disseminate Istat aggregate data.
All data currently available on I.Stat have been moved to IstatData, which allows to browse the same contents improved with charts, maps and thematic data summaries.
The platform uses the open source tools "Data Browser" and "Meta & Data Manager" developed by Istat (https://sdmxistattoolkit.github.io) following the international standard SDMX (Statistical Data and Metadata eXchange) for the exchange and sharing of data and statistical metadata.

**List of files:**
The datasets used  were obtained from the Population and Households section and the Foreigners and Immigrants or Migrations section, located within the respective path on the website.

| ID  | Dataset link | Name |
| ------------- | ------------- | ------------- | 
| D1  | [esloradati.istat.it](https://esploradati.istat.it/databrowser/#/en/dw/categories/IT1,POP,1.0/POP_FOREIGNIM/DCIS_POPSTRRES1/IT1,29_7_DF_DCIS_POPSTRRES1_1,1.0)  | `Italy, regions, provinces (IT1,29_7_DF_DCIS_POPSTRRES1_1,1.0)`; Population on 1st January |
| D2  | [esloradati.istat.it](https://esploradati.istat.it/databrowser/#/en/dw/categories/IT1,POP,1.0/POP_FOREIGNIM/DCIS_POPSTRBIL1/IT1,29_316_DF_DCIS_POPSTRBIL1_1,1.0) | `Italy, regions, provinces (IT1,29_316_DF_DCIS_POPSTRBIL1_1,1.0)`; Balance | 
| D3  | [esloradati.istat.it](https://esploradati.istat.it/databrowser/#/en/dw/categories/IT1,POP,1.0/POP_FOREIGNIM/DCIS_ACQCITIZ/IT1,29_849_DF_DCIS_ACQCITIZ_1,1.0) | `Process and age class (IT1,29_849_DF_DCIS_ACQCITIZ_1,1.0)`; Foreigners who acquired Italian citizenship | 
| D4  | [esloradati.istat.it](https://esploradati.istat.it/databrowser/#/en/dw/categories/IT1,POP,1.0/POP_MIGRATIONS/DCIS_MIGRAZIONI/IT1,28_185_DF_DCIS_MIGRAZIONI_2,1.0) | `Immigrants - citizenship (IT1,28_185_DF_DCIS_MIGRAZIONI_2,1.0)` | 
| D5  | [esloradati.istat.it](https://esploradati.istat.it/databrowser/#/en/dw/categories/IT1,POP,1.0/POP_FOREIGNIM/DCIS_PERMSOGG1/IT1,29_348_DF_DCIS_PERMSOGG1_1,1.0) | `Type of residence permit and citizenship (IT1,29_348_DF_DCIS_PERMSOGG1_1,1.0)`; Residence permits on 1st January |



**Noi Italia 2024**

url: https://noi-italia.istat.it/home.php

An overview of official statistics on the various demographic, economic, social and environmental aspects of Italy, the regional differences that characterise it and its place in the European context.
The information offer is organised into 6 thematic areas (Population and society, Education and work, Health and welfare, Industry and services, Environment and agriculture, Economy and public finance), divided into 19 sectors accompanied by descriptive summaries on the trend of phenomena and territorial differences, also enriched by graphs, glossary and references to useful publications and links.

**List of files**
The datasets used were obtained from the POPOLAZIONE E SOCIETÀ section and the STRANIERI section, located within the respective path on the website.

| ID  | Dataset link | Name |
| ------------- | ------------- | ------------- | 
| D6  | [noi-italia.istat.it](https://noi-italia.istat.it/pagina.php?L=0&categoria=4&dove=ITA)  | `NI2024-Stranieri_altri_dati_2`; Education levels and age groups (15-64 years) of both domestic and foreign populations |

**Immigrants.Stat**

url: http://stra-dati.istat.it/Index.aspx

Immigrants.Stat is the data warehouse that collects and organizes the statistics produced by Istat on foreign immigrants and new citizens in order to make them more easily accessible to the different types of users involved (researchers, policy makers, journalists, citizens). It is a work in progress as the system will adapt to new information needs.

 **List of files:**

| ID  | Dataset link | Name |
| ------------- | ------------- | ------------- | 
| D7  | [stra-dati.istat.it](http://stra-dati.istat.it/Index.aspx?lang=en&SubSessionId=1e10059f-62b5-4107-bb48-38b281ae5de0)  | `DCCV_OCCUPATIT1_12012025111941696`; Employment (thousands): Data by highest level of education attained, sub national level - foreigners |
| D8  | [stra-dati.istat.it](http://stra-dati.istat.it/?lang=en&SubSessionId=9168695d-68df-4465-8170-642f0da567c1#)  | `DCCV_OCCUPATIT1_12012025110421591`;  Employment: Data by gender, full-time/part-time, sub national level - foreigners |
| D9  | [stra-dati.istat.it](http://stra-dati.istat.it/?lang=en&SubSessionId=9168695d-68df-4465-8170-642f0da567c1#)  | `DCCV_OCCUPATIT1_12012025110704049`;  Employment: Data on employees by gender, sub national level - foreigners |
| D10  | [stra-dati.istat.it](http://stra-dati.istat.it/?lang=en&SubSessionId=9168695d-68df-4465-8170-642f0da567c1#)  | `DCCV_TAXOCCU1_12012025110922125`;  Employment rate: Data by gender, highest level of education attained, sub national level - foreigners |
| D11  | [stra-dati.istat.it](http://stra-dati.istat.it/?lang=en&SubSessionId=9168695d-68df-4465-8170-642f0da567c1#)  | `DCCV_TAXDISOCCU1_12012025111208359`;  Unemployment rate: Data by highest level of education attained, sub national level - foreigners  |
| D12  | [stra-dati.istat.it](http://stra-dati.istat.it/?lang=en&SubSessionId=9168695d-68df-4465-8170-642f0da567c1#)  | `DCIS_PERMSOGG1_12012025111539693`;  Residence permits of non-EU citizens: Annual inflows of non-EU citizens by asylum granted, asylum application and humanitarian reasons  |


**OECD: Organisation for Economic Co-operation and Development**

url: https://www.oecd.org/

The OECD (Organisation for Economic Co-operation and Development) is a forum and knowledge hub for data, analysis and best practices in public policy. We work with over 100 countries across the world to build stronger, fairer and cleaner societies - helping to shape better policies for better lives.

**List of files:**

| ID  | Dataset link | Name |
| ------------- | ------------- | ------------- |
| D13  | [data-explorer.oecd.org](https://data-explorer.oecd.org/vis?lc=en&fs%5B0%5D=Topic%2C1%7CSociety%23SOC%23%7CMigration%23SOC_MIG%23&pg=0&fc=Topic&bp=true&snb=6&vw=ov&df%5Bds%5D=dsDisseminateFinalDMZ&df%5Bid%5D=DSD_MIG%40DF_MIG&df%5Bag%5D=OECD.ELS.IMD&df%5Bvs%5D=1.0&dq=ITA..A.B11....&pd=2019%2C&to%5BTIME_PERIOD%5D=false&ly%5Bcl%5D=TIME_PERIOD&ly%5Brs%5D=SEX&ly%5Brw%5D=CITIZENSHIP)  | `OECD.ELS.IMD,DSD_MIG@DF_MIG,1.0+ITA..A.B11`; International migration database, Inflows of foreign population; Reference Area: Italy | 
| D14  | [data-explorer.oecd.org](https://data-explorer.oecd.org/vis?lc=en&fs%5B0%5D=Topic%2C1%7CSociety%23SOC%23%7CMigration%23SOC_MIG%23&pg=0&fc=Topic&bp=true&snb=6&df%5Bds%5D=dsDisseminateFinalDMZ&df%5Bid%5D=DSD_MIG_INT%40DF_MIG_INT_TEMP&df%5Bag%5D=OECD.ELS.IMD&df%5Bvs%5D=1.0&dq=.A...&lom=LASTNPERIODS&lo=10&to%5BTIME_PERIOD%5D=false&vw=tb)  | `OECD.ELS.IMD,DSD_MIG_INT@DF_MIG_INT_TEMP,1.0+.A`; Standardised inflows of temporary migrants, Migration flows by category | 
| D15  | [data-explorer.oecd.org](https://data-explorer.oecd.org/vis?df%5Bds%5D=dsDisseminateFinalDMZ&df%5Bid%5D=DSD_MIG_INT%40DF_MIG_INT_PER&df%5Bag%5D=OECD.ELS.IMD&df%5Bvs%5D=1.0&dq=.A...&lom=LASTNPERIODS&lo=10&to%5BTIME_PERIOD%5D=false)  | `OECD.ELS.IMD,DSD_MIG_INT@DF_MIG_INT_PER,1.0+ITA.A...`; Standardised inflows of permanent-type migrants, Migration flows by category |

### 3.2. Mashed-up dataset <a name="s-3-2"></a>

In order to manage the mash-up of different datasets with different licenses, we followed the [Guidelines for Open Data provided by the EU.](https://eur-lex.europa.eu/legal-content/EN/TXT/?qid=1561563110433&uri=CELEX:32019L1024)
The datasets were then merged and processed into:

| Primary datasets  | Mashed-up dataset | 
| ------------- | ------------- | 
| D4, D5, D15 | [DeMi: Trends by Country and Residence Permits](https://github.com/mjavadf/DeMi/blob/main/datasets/mashup/italy_immigration_trends_by_country_and_permit.csv) | 
| D8, D10, D11 | [DeMi: Trends by Education Level, Employment and Unemployment](https://github.com/mjavadf/DeMi/blob/main/datasets/mashup/italy_immigration_trends_by_demographic_profiles.csv)  | 

The process of merging is presented through [Jupyter Notebook](https://jupyter.org) and can be found [here](https://github.com/mjavadf/DeMi/blob/main/DeMi.ipynb). 


# 4. Quality analysis of the datasets <a name="quality-analysis"></a>
To conduct the quality analysis, we adhered to the [ISO/IEC 25012 standard](https://iso25000.com/index.php/en/iso-25000-standards/iso-25012), which outlines 15 key data quality characteristics, as shown in the picture below. 

![Picture 1](https://github.com/user-attachments/assets/58a8f18e-d348-499f-9db5-b64ca6c3133f)

These characteristics are grouped into two main categories: Inherent Data Quality and System-Dependent Data Quality. For this analysis, we focused exclusively on *Inherent Data Quality*, as it pertains to the intrinsic properties of the data itself, independent of any specific system or context. This focus allows us to evaluate the dataset's accuracy, completeness, consistency, credibility, and currentness comprehensively.

During the analysis, we observed that several columns contained a significant proportion of missing values. To quantify this issue, we calculated the percentage of completeness for each dataset using a [specialized algorithm](https://github.com/mjavadf/DeMi/blob/main/datasets/completeness.py), created with python. The detailed results of this evaluation are provided below.


| **Dataset**        | **Accuracy** | **Completeness** | **Consistency** | **Credibility** | **Currentness** |
|--------------------|--------------|------------------|-----------------|-----------------|-----------------|
| **D1, D2, D3, D4, D5** | The datasets seem to contain population statistics, but without further context or a known reference, verifying the accuracy of the `OBS_VALUE` column is difficult. However, the data appears numerical and follows a consistent pattern for different years. In **D4**, the dataset includes a `CITIZENSHIP` value of 999, which may represent unknown or unspecified values. | There are missing values in several columns, including `OBS_STATUS`, `NOTE_*`, and other metadata fields. While some missing values may be expected (e.g., supplementary notes), the lack of completeness in the metadata columns limits the context for interpreting the data. | The datasets are logically structured, and the rows are consistent in terms of columns. However, missing data in `NOTE_*` columns raises the possibility of inconsistency in additional attributes or annotations. | The datasets come from a reliable source (it includes terms like `IT1:29_7_DF` which are references to an official dataset identifier from a trusted body). | The datasets include time periods ranging from 2019 to 2023, so they appear to be up-to-date in the context of our project. |
| **D6** **  | The dataset contains percentage values for foreign and Italian populations by age group and education level. The values in the `Foreign_Percentage` and `Italian_Percentagecolumns` seem plausible. | The dataset appears complete for the given columns (`Year`, `Age_Group`, `Education_Level`, etc.) and contains no missing values for these fields. | The dataset is consistent in structure and the values for `Foreign_Percentage` and `Italian_Percentage` seem logically coherent when compared to each other. | The dataset appears reliable. | The dataset includes time periods ranging from 2019 to 2023, so it appears to be up-to-date in the context of our project. |
| **D7, D8, D9, D10, D11, D12** | The data in the `Value` column appears reasonable for employment statistics. | The datasets appear to be complete for the columns provided, with no missing data for critical fields like `TIME`, `Age class`, `CITTADINANZA`, and `Value`. However, columns such as `Flag Code`s and `Flags` have missing values, which may affect the completeness of the metadata. | The datasets are internally consistent, with time periods (`TIME`) and corresponding values (`Value`) aligning correctly. | The datasets appear to come from a credible source. | The datasets include time periods ranging from 2019 to 2023, so they appear to be up-to-date in the context of our project. |
| **D13, D14, D15** | The datasets provide migration statistics, including values such as `OBS_VALUE`, which represent migration figures by citizenship. | The datasets contain several columns with missing values, such as `TIME_PERIOD`, `OBS_VALUE`, and `OBS_STATUS`. | The dataset is consistent in structure, with migration data segmented by country of citizenship, time period, and observation value. The use of `OBS_STATUS` and `DECIMALS` suggests that the dataset is designed for consistent reporting. However, the missing values in `TIME_PERIOD` could affect the overall consistency in terms of time-based analysis. | Given the dataset is from the OECD's International Migration Database, it is likely to be credible. | The datasets include time periods ranging from 2019 to 2023, so they appear to be up-to-date in the context of our project. | 

** During the initial analysis of D6, we noticed that the csv file had structural inconsistencies that rendered the calculation of completeness percentages infeasible. To address these challenges and enable accurate analysis, a preprocessing step was performed using a [python script](https://github.com/mjavadf/DeMi/blob/main/datasets/formattingCSV.py), [the formatted file](https://github.com/mjavadf/DeMi/blob/main/datasets/NoiItalia2024/output_file.csv) was then uploaded and analyzed. 


### Column Descriptions:
* **Completeness**: The extent to which all required data is present. The dataset may have missing values or incomplete fields that affect its usefulness.
* **Accuracy**: The degree to which the data correctly represents the real-world values. In some cases, external validation is required to assess this fully.
* **Coherence**: The extent to which the data is logically coherent and aligns with other related data. Missing or inconsistent data can reduce the overall coherence.
* **Credibility**: The trustworthiness of the source of the data. Ideally, the dataset should come from a recognized and reliable source.
* **Currentness**: The timeliness of the data. A dataset is more valuable when it includes up-to-date information.

### Completeness Algorithm Results

The completeness of each dataset was assessed by identifying null values. Null values were determined by checking each cell for missing or empty data, including specific indicators of missing values such as `NaN`, `' '`, `''`, `'-'`, and `'.'`. The following table provides the total values, null values, and completeness percentage for each dataset:

| **Dataset** | **Total Values** | **Null Values** | **Completeness (%)** |
|-------------|------------------|-----------------|----------------------|
| **D1**      | 4,276,044        | 2,028,780       | 52.55%               |
| **D2**      | 639,180          | 297,780         | 53.41%               |
| **D3**      | 8,568            | 4,488           | 47.62%               |
| **D4**      | 331,992          | 172,153         | 48.15%               |
| **D5**      | 90,175           | 46,839          | 48.06%               |
| **D6**      | 540              | 0               | 100.0%               |
| **D7**      | 24,024           | 3,696           | 84.62%               |
| **D8**      | 20,250           | 2,700           | 86.67%               |
| **D9**      | 22,950           | 2,700           | 88.24%               |
| **D10**     | 20,400           | 2,400           | 88.24%               |
| **D11**     | 30,195           | 4,026           | 86.67%               |
| **D12**     | 361,605          | 48,214          | 86.67%               |
| **D13**     | 271,950          | 18,223          | 93.30%               |
| **D14**     | 41,472           | 3,491           | 91.58%               |
| **D15**     | 41,184           | 3,447           | 91.63%               |

# 5. Legal analysis
### Original Datasets
The original datasets used to cover the different themes of this project are listed in [Section 3.1. ](#section-3-1)

### Legal checklist<a name="legal-analysis"></a>
The fields with an asterisk (*) have to be further explained in the notes below.

| | To check | D1, D2, D3, D4, D5 | D6 | D7, D8, D9, D10, D11, D12 | D13, D14, D15 |
| --- | --- | --- | --- | --- | --- |
| **Privacy issues** |
| | 1.1 Is the dataset free of any personal data as defined in the Regulation (EU) 2016/679? | Yes | Yes | Yes | Yes |
| | 1.2 Is the dataset free of any indirect personal data that could be used for identifying the natural person? If so, is there a law that authorizes the PA to release them? Or any other legal basis? Identify the legal basis. | Yes | Yes | Yes | Yes |
| | 1.3 Is the dataset free of any particular personal data (art. 9 GDPR)? If so is there a law that authorizes the PA to release them? | Yes | Yes | Yes | Yes |
| | 1.4 Is the dataset free of any information that combined with common data available on the web, could identify the person? If so, is there a law that authorizes the PA to release them? | Yes | Yes | Yes | Yes |
| | 1.5 Is the dataset free of any information related to human rights (e.g. refugees, witness protection, etc.)? | | | | |
| | 1.6 Do you use a tool for calculating the range of the risk of deanonymization? Do you anonymize the dataset? With which technique? Did you check the three mandatory parameters: singling out, linking out, inference out? | No* | No* | No* | No* |
| | 1.7 Are you using geolocalization capabilities? Do you check that the geolocalization process can’t identify single individuals in some circumstances? | | | | |
| | 1.8 Did you check that the open data platform respect all the privacy regulations (registration of the end-user, profiling, cookies, analytics, etc.)? | Yes | Yes | Yes | No* |
| | 1.9 Do you know who are in your open data platform the Controller and Processor of the privacy data of the system? | Yes, Istituto Nazionale di Statistica (Istat) | Yes, Istat | Yes, Istat | Yes, OECD |
| | 1.10 Where the datasets are physically stored (country and jurisdiction)? Do you have a cloud computing platform? Do you have checked the privacy regulation of the country where the dataset are physically stored? (territoriality) | Italy (Italian jurisdiction), no, yes | Italy (Italian jurisdiction), no, yes | Italy (Italian jurisdiction), no, yes | France (French jurisdiction), no, yes |
| | 1.11 Do you have non-personal data? Are you sure that are not "mixed data"? | There are mixed data | There are mixed data | There are mixed data | There are mixed data |
| **Intellectual Property Rights of the dataset** | | |
| | 2.1 Do you have created and generated the dataset? | No | No | No | No |
| | 2.2 Are you the owner of the dataset? Who is the owner? | No, Istat | No, Istat | No, Istat | No, OECD |
| | 2.3 Are you sure to not use third party data without the proper authorization and license? Are the dataset free from third party licenses or patents? | Yes | Yes | Yes | Yes |
| | 2.4 Do you have checked if there are some limitations in your national legal system for releasing some kind of datasets with an open license? | Yes | Yes | Yes | Yes |
| **License** | | |
| | 3.1 Do you release the dataset with an open data license? In case of the use of CC0 do you check that you have all the right necessary for this particular kind of license (e.g., jurisdiction)? | Yes | Yes | Yes | Yes |
| | 3.2 Do you include the clause: "In any case the dataset can’t be used for re-identifying the person"? | No | No | No | No |
| | 3.3 Do you release the API (in case you have) with an open source license? | N/A | N/A | N/A | N/A |
| | 3.4 Do you check that the open data/API platform licence regime is compliance with your IPR policy? Do you have all the licences related to the open data platform/API software? | Yes | Yes | Yes | Yes |
| **Limitations on public access** | | |
| | 4.1 Do you check that the dataset concerns your institutional competences, scope and finality? Do you check if the dataset concerns other public administration competences? | Yes | Yes | Yes | Yes |
| | 4.2 Do you check the limitations for the publication stated by your national legislation or by the EU directives? | Yes | Yes | Yes | Yes |
| | 4.3 Do you check if there are some limitations connected to the international relations, public security or national defence? | Yes | Yes | Yes | Yes |
| | 4.4 Do you check if there are some limitations concerning the public interest? | Yes | Yes | Yes | Yes |
| | 4.5 Do you check the international law limitations? | Yes | Yes | Yes | Yes |
| | 4.6 Do you check the INSPIRE law limitations for the spatial data? | | | | |
| **Economical Conditions** | | |
| | 5.1 Do you check that the dataset could be released for free? | Yes | Yes | Yes | Yes |
| | 5.2 Do you check if there are some agreements with some other partners in order to release the dataset with a reasonable price? | No | No | No | No |
| | 5.3 Do you check if the open data platform terms of service include a clause of “non liability agreement” regarding the dataset and API provided? | Yes | Yes | Yes | Yes |
| | 5.4 In case you decide to release the dataset to a reasonable price do you check if the limitation imposed by the new directive 2019/1024/EU are respected? Are you able to calculate the “marginal cost”? Are you able to justify the “reasonable return on investment” limited to cover the costs of collection, production, reproduction, dissemination, preservation and rights clearance? There is a national law that justify your public administration to apply the “reasonable return of investment”? | N/A | N/A | N/A | N/A |
| | 5.5 In case you decide to release the dataset to a reasonable price do you check the e-Commerce directive1 and regulation? | N/A | N/A | N/A | N/A |
| **Temporary aspects** | | |
| | 6.1 Do you have a temporary policy for updating the dataset? | | | | |
| | 6.2 Do you have some mechanism for informing the end-user that the dataset is updated at a given time to avoid mis-usage and so potential risk of damage? | | | | |
| | 6.3 Did you check if the dataset for some reason can’t be indexed by the research engines (e.g. Google, Yahoo, etc.)? | | | | |
| | 6.4 In case of personal data, do you have a reasonable technical mechanism for collecting request of deletion (e.g. right to be forgotten)? | | | | |

#### Notes

1.6 : we do not use a tool for calculating the range of the risk of deanonymization as anonymization is not necessary for our dataset. The dataset does not contain any personal data that requires anonymization. Therefore, the three mandatory parameters—singling out, linking out, and inference out—are not applicable to our case.

1.7 : According to [OECD Privacy Policy](https://www.oecd.org/en/about/privacy.html), personal data is collected directly via user input and indirectly through cookies for personalization. However, the policy lacks clarity on user consent and GDPR compliance, requiring further verification of adherence to privacy regulations.

### Licenses
Below is a quick overview of the licensing terms for each dataset used in this project.

**Primary datasets**

| **Dataset** | **License** | 
|-------------|------------------|
| **D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12**      | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) |
| **D13, D14, D15**  | [OECD’s Terms and Conditions*](https://www.oecd.org/en/about/terms-conditions.html) |

Most of the data (D1–D12) is available under the [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) license, which permits to:

* Share — copy and redistribute the material in any medium or format for any purpose, even commercially
* Adapt — remix, transform, and build upon the material for any purpose, even commercially

Under the following terms:
* Attribution — You must give appropriate credit , provide a link to the license, and indicate if changes were made . You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
* No additional restrictions — You may not apply legal terms or technological measures that legally restrict others from doing anything the license permits.
* No permission is necessary to hyperlink to pages on this website.
Images, logos (including Istat logo), trademarks and other content owned by third parties belong to their respective owners and cannot be reproduced without their consent.

A few datasets (D13–D15) fall under the [OECD’s Terms and Conditions*](https://www.oecd.org/en/about/terms-conditions.html), meaning they can generally be used for non-commercial purposes with source attribution, but commercial use or wider distribution may require prior written permission from the OECD. 

**Mashed-up datasets**
| **Dataset** | **License** | 
|-------------|------------------|
| **DeMi: Trends by Country of Origin and Residence Permits**      | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.en) |
| **DeMi: Trends by Education Level, Employment and Unemployment**      | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.en) |


With [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.en), you are free to:

* Share — copy and redistribute the material in any medium or format for any purpose, even commercially.
* Adapt — remix, transform, and build upon the material for any purpose, even commercially.
The licensor cannot revoke these freedoms as long as you follow the license terms.

Under the following terms:
* Attribution — You must give appropriate credit , provide a link to the license, and indicate if changes were made . You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
* ShareAlike — If you remix, transform, or build upon the material, you must distribute your contributions under the same license as the original.
* No additional restrictions — You may not apply legal terms or technological measures that legally restrict others from doing anything the license permits.

### Clarification on Licensing for Istat Portals
While IstatData (D1–D5), Not Italia 2024 (D6), and Immigrants.Stat (D7–D12) do not explicitly display licensing information on their respective pages, these portals are known to be part of Istat. Based on this, we infer that the [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) applies to all datasets from these sources. Additionally, it's important to note that [Istat's datasets](https://www.istat.it/en/data/datasets/) are typically released in a preliminary form immediately following survey completions, and are not issued at regular intervals. 

### Purpose 

**Primary datasets**

**D1** – Official demographic data of foreign residents in Italy as of January 1st each year.

**D2** – Tracks various demographic indicators such as census population counts, live births, deaths, and migration statistics.

**D3** – Analyzes citizenship acquisition processes, categorized by age groups.

**D4** – Provides statistics on immigrants in Italy, classified by their original citizenship.

**D5** – Focuses on immigrants' citizenship status with an emphasis on different types of residence permits.

**D6** – Comparative analysis of educational attainment levels between domestic and foreign populations, specifically for the working-age group (15-64 years).

**D7** – Employment statistics segmented by foreigners' highest educational attainment.

**D8** – Employment data categorized by gender and employment type (full-time or part-time).

**D9** – Employment of foreign men and women at a regional level, highlighting gender disparities in the labor market.

**D10** – Employment rates among foreigners based on education and gender at a sub-national level.

**D11** – Unemployment rates among foreigners categorized by educational qualifications and regional distribution, identifying skill gaps.

**D12** – Annual data on the inflow of non-EU citizens granted residence permits for asylum, humanitarian, or other reasons.

**D13** – Annual volume of non-Italian nationals entering Italy for residency purposes.

**D14** – Tracks temporary migration, including workers, students, and short-term visa holders.

**D15** – Standardized data on the inflows of permanent-type migrants, detailing migration flows by category and intention of long-term residency.

**Mashed-up datasets**

**DeMi: Trends by Country and Residence Permits** – Examines the evolution of foreign residents, with a focus on gender, country of origin, temporary and permanent migration categories.

**DeMi: Trends by Education Level, Employment and Unemployment** – Explores employment and education trends among immigrants, with a focus on gender, education level, employment/unemployment percentage and work type.


# 6. Ethics analysis<a name="ethics-analysis"></a>

The process of ethical analysis of datasets is crucial for maintaining trust and safeguarding the interests of individuals whose data are involved, especially in sensitive areas like ours, demographics and migration.

**Istat.Data, Noi Italia 2024, Immigrants.Stat**: All institutions of Istat comply with GDPR, highlighting its commitment to processing personal data transparently and responsibly. As the designated data controller, Istat ensures that data usage is strictly tied to public interest tasks and is legally justified. The data collected, including IP addresses and system details, are essential for operational purposes and statistical analysis, with a retention period that does not exceed ninety days to minimize privacy risks.
For further details on their data protection policies, you can visit [Istat's Privacy Page](https://www.istat.it/privacy/).

Istat's adherence to the highest quality standards is mandated both at a national and European level. It operates under the fundamental principles of official statistics set by the European Parliament and Council with [Regulation (EC) No. 223/2009](https://www.eumonitor.eu/9353000/1/j4nvhdlglbmvdzx_j9vvik7m1c3gyxp/vm4nk8maqayk#:~:text=(1)%20Regulation%20(EC),and%20dissemination%20of%20European%20statistics.). Moreover, these principles are echoed in the United Nations Economic Commission for Europe's regulations and further supported by the United Nations Statistical Commission. For further details on their data protection policies, you can visit [Istat's Activity Page.](https://www.istat.it/listituto/attivita/)

**OECD**: 
The OECD maintains personal data protection standards as part of its commitment to safeguarding individual privacy across its operations. Established under the framework of the [1980 OECD Privacy Guidelines](https://legalinstruments.oecd.org/en/instruments/OECD-LEGAL-0188) and updated in 2013, these standards ensure that data handling within OECD follow principles of transparency, legality, and necessity. 
The organization processes personal data to support various public interest missions, including managing staff-related benefits, [recruitment](https://www.oecd.org/en/about/careers/data-protection-notice-for-recruitment.html), and facilitating participation in policy-making through surveys like [PISA](https://www.oecd.org/en/about/programmes/pisa/pisa-data.html) and assessment platforms such as [PILA](https://pilaproject.org). 

The [OECD Data Protection Rules](https://www.oecd.org/content/dam/oecd/en/about/data-protection/Decision-of-the-SG-on-Personal-Data-Protection.pdf), established by the Secretary-General's decision, mandate that all staff must protect personal data through transparent and appropriate measures. These rules apply to any personal data processing conducted by or on behalf of the OECD and are detailed in [Annex XII](https://www.oecd.org/content/dam/oecd/en/about/careers/Staff_Rules_and_Regulations_EN.pdf) of the Staff Rules and Regulations. They require personal data to be processed transparently and for legitimate purposes, ensuring data is adequate, relevant, up-to-date, and retained only as long as necessary. For further details on their data protection policies, you can visit [OECD's Personal data protection Page.](https://www.oecd.org/en/about/data-protection.html)

# 7. Technical analysis<a name="technical-analysis"></a>

### Formats, metadata, provenance URI

The following is a resume of our original datasets' formats, metadata, provenance, and URI. Regarding metadata, certain datasets are either devoid of metadata or only contain metadata that can be read by humans. However, using machine-readable metadata is strongly advised by Article 9 Comma 1 of regulation [EU 2019/1024](https://eur-lex.europa.eu/eli/dir/2019/1024/oj).

#### D1, D2, D3, D4, D5
**Format**: Excel, CSV, JSON, SDMX  
**Metadata**: Provided in the SDMX format, which is machine-readable and can be used for automated processing.  
**URI**s:  
- [esloradati.istat.it](https://esploradati.istat.it/databrowser/#/en/dw/categories/IT1,POP,1.0/POP_FOREIGNIM/DCIS_POPSTRRES1/IT1,29_7_DF_DCIS_POPSTRRES1_1,1.0)  
- [esloradati.istat.it](https://esploradati.istat.it/databrowser/#/en/dw/categories/IT1,POP,1.0/POP_FOREIGNIM/DCIS_POPSTRBIL1/IT1,29_316_DF_DCIS_POPSTRBIL1_1,1.0)  
- [esloradati.istat.it](https://esploradati.istat.it/databrowser/#/en/dw/categories/IT1,POP,1.0/POP_FOREIGNIM/DCIS_ACQCITIZ/IT1,29_849_DF_DCIS_ACQCITIZ_1,1.0)  
- [esloradati.istat.it](https://esploradati.istat.it/databrowser/#/en/dw/categories/IT1,POP,1.0/POP_MIGRATIONS/DCIS_MIGRAZIONI/IT1,28_185_DF_DCIS_MIGRAZIONI_2,1.0)  
- [esloradati.istat.it](https://esploradati.istat.it/databrowser/#/en/dw/categories/IT1,POP,1.0/POP_FOREIGNIM/DCIS_PERMSOGG1/IT1,29_348_DF_DCIS_PERMSOGG1_1,1.0)    

**Provenance**:  
- [esloradati.istat.it](https://esploradati.istat.it/databrowser/#/en/dw/categories/IT1,POP,1.0/POP_FOREIGNIM/DCIS_POPSTRRES1/IT1,29_7_DF_DCIS_POPSTRRES1_1,1.0)  
- [esloradati.istat.it](https://esploradati.istat.it/databrowser/#/en/dw/categories/IT1,POP,1.0/POP_FOREIGNIM/DCIS_POPSTRBIL1/IT1,29_316_DF_DCIS_POPSTRBIL1_1,1.0)  
- [esloradati.istat.it](https://esploradati.istat.it/databrowser/#/en/dw/categories/IT1,POP,1.0/POP_FOREIGNIM/DCIS_ACQCITIZ/IT1,29_849_DF_DCIS_ACQCITIZ_1,1.0)  
- [esloradati.istat.it](https://esploradati.istat.it/databrowser/#/en/dw/categories/IT1,POP,1.0/POP_MIGRATIONS/DCIS_MIGRAZIONI/IT1,28_185_DF_DCIS_MIGRAZIONI_2,1.0)  
- [esloradati.istat.it](https://esploradati.istat.it/databrowser/#/en/dw/categories/IT1,POP,1.0/POP_FOREIGNIM/DCIS_PERMSOGG1/IT1,29_348_DF_DCIS_PERMSOGG1_1,1.0)  

#### D6
**Format**: CSV  
**Metadata**: The dataset does not contain machine-readable metadata  
**URI**: 
- [Popolazione e società > Stranieri](https://noi-italia.istat.it/pagina.php?L=0&categoria=4&dove=ITA)  

**Provence**: 
- [Istat/lavoro](https://www.istat.it/it/lavoro-e-retribuzioni "https://www.istat.it/it/lavoro-e-retribuzioni")  
- [Istat/demografia](https://demo.istat.it/ "https://demo.istat.it/")  
- [Istat/stranieri](https://www.istat.it/it/archivio/stranieri "https://www.istat.it/it/archivio/stranieri")  
- [Istat/immigrati](http://stra-dati.istat.it/ "http://stra-dati.istat.it/")  
- [Istat/datawarehouse](http://dati.istat.it/ "http://dati.istat.it/")  
- [Eurostat/labour market](https://ec.europa.eu/eurostat/web/lfs/statistics-illustrated "https://ec.europa.eu/eurostat/web/lfs/statistics-illustrated")  
- [Eurostat/migrant integration](http://ec.europa.eu/eurostat/statistics-explained/index.php/Migrant_integration_statistics "http://ec.europa.eu/eurostat/statistics-explained/index.php/Migrant_integration_statistics")

#### D7, D8, D9, D10, D11, D12  
**Format**: CSV, JSON, SDMX  
**Metadata**: Provided in the SDMX format with Developer API.  
**URI**: [Statistice Istat](http://stra-dati.istat.it/ "http://stra-dati.istat.it/")  
**Provenance**: [Statistiche Istat](http://stra-dati.istat.it/ "http://stra-dati.istat.it/")  
*Note*: The ISTAT portal does not offer direct links to the datasets. Access to the datasets was obtained through the http://stra-dati.istat.it/ portal, which contains older data (prior to 2019).

#### D13, D14, D15  
**Format**: CSV, JSON, SDMX  
**Metadata**: Provided in the SDMX format with Developer API.  
**URI**:  
- [International migration database, Inflows of foreign population](https://data-explorer.oecd.org/vis?lc=en&fs%5B0%5D=Topic%2C1%7CSociety%23SOC%23%7CMigration%23SOC_MIG%23&pg=0&fc=Topic&bp=true&snb=6&vw=ov&df%5Bds%5D=dsDisseminateFinalDMZ&df%5Bid%5D=DSD_MIG%40DF_MIG&df%5Bag%5D=OECD.ELS.IMD&df%5Bvs%5D=1.0&dq=ITA..A.B11....&pd=2019%2C&to%5BTIME_PERIOD%5D=false&ly%5Bcl%5D=TIME_PERIOD&ly%5Brs%5D=SEX&ly%5Brw%5D=CITIZENSHIP)  
- [Standardised inflows of temporary migrants](https://data-explorer.oecd.org/vis?lc=en&fs%5B0%5D=Topic%2C1%7CSociety%23SOC%23%7CMigration%23SOC_MIG%23&pg=0&fc=Topic&bp=true&snb=6&df%5Bds%5D=dsDisseminateFinalDMZ&df%5Bid%5D=DSD_MIG_INT%40DF_MIG_INT_TEMP&df%5Bag%5D=OECD.ELS.IMD&df%5Bvs%5D=1.0&dq=.A...&lom=LASTNPERIODS&lo=10&to%5BTIME_PERIOD%5D=false&vw=tb)  
- [Standardised inflows of permanent-type migrants](https://data-explorer.oecd.org/vis?df%5Bds%5D=dsDisseminateFinalDMZ&df%5Bid%5D=DSD_MIG_INT%40DF_MIG_INT_PER&df%5Bag%5D=OECD.ELS.IMD&df%5Bvs%5D=1.0&dq=.A...&lom=LASTNPERIODS&lo=10&to%5BTIME_PERIOD%5D=false)  

**Provenance**:  
- [International migration database, Inflows of foreign population](https://data-explorer.oecd.org/vis?lc=en&fs%5B0%5D=Topic%2C1%7CSociety%23SOC%23%7CMigration%23SOC_MIG%23&pg=0&fc=Topic&bp=true&snb=6&vw=ov&df%5Bds%5D=dsDisseminateFinalDMZ&df%5Bid%5D=DSD_MIG%40DF_MIG&df%5Bag%5D=OECD.ELS.IMD&df%5Bvs%5D=1.0&dq=ITA..A.B11....&pd=2019%2C&to%5BTIME_PERIOD%5D=false&ly%5Bcl%5D=TIME_PERIOD&ly%5Brs%5D=SEX&ly%5Brw%5D=CITIZENSHIP)  
- [Standardised inflows of temporary migrants](https://data-explorer.oecd.org/vis?lc=en&fs%5B0%5D=Topic%2C1%7CSociety%23SOC%23%7CMigration%23SOC_MIG%23&pg=0&fc=Topic&bp=true&snb=6&df%5Bds%5D=dsDisseminateFinalDMZ&df%5Bid%5D=DSD_MIG_INT%40DF_MIG_INT_TEMP&df%5Bag%5D=OECD.ELS.IMD&df%5Bvs%5D=1.0&dq=.A...&lom=LASTNPERIODS&lo=10&to%5BTIME_PERIOD%5D=false&vw=tb)  
- [Standardised inflows of permanent-type migrants](https://data-explorer.oecd.org/vis?df%5Bds%5D=dsDisseminateFinalDMZ&df%5Bid%5D=DSD_MIG_INT%40DF_MIG_INT_PER&df%5Bag%5D=OECD.ELS.IMD&df%5Bvs%5D=1.0&dq=.A...&lom=LASTNPERIODS&lo=10&to%5BTIME_PERIOD%5D=false)

# 8. Sustainability of the update the datasets over time <a name="sustainability"></a>

This catalogue was created as part of "Open Access and Digital Ethics" course at the [University of Bologna](https://www.unibo.it) and is not actively maintained by our team; however, the underlying datasets — focused on migration in Italy and sourced from ISTAT and OECD — are regularly updated by their respective institutions. 
Our automated scripts, which remain available and licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.en), can be rerun on new files whenever a dataset is updated. 
Sustainability is a collective responsibility. We encourage anyone who notices an updated input file to notify us so we can use our automated process to update the catalogue accordingly. Contributions and updated files submitted via our [GitHub project](https://github.com/mjavadf/DeMi/tree/main) will be reviewed and added if they meet our standards, ensuring that the catalogue remains a relevant and evolving resource.

# 9. Visualization <a name="visualization"></a>


# 10. RDF assertion of metadata <a name="rdf"></a>
For encoding metadata, we followed [Data Catalog Vocabulary (DCAT) - Version 2](https://www.w3.org/TR/vocab-dcat-2/). For validation, we used [W3C RDF Validator](https://www.w3.org/RDF/Validator/). 

You can find the file wtih encoding of all primary and mashed-up datasets here. 

# 11. Conclusions <a name="conclusions"></a>
