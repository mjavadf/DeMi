# 1.	Introduction 

DeMi (Decoding Migration) has been carried out for the exam "Open Access and Digital Ethics" as a part of the [Digital Humanities and Digital Knowledge course](https://corsi.unibo.it/2cycle/DigitalHumanitiesKnowledge) at the University of Bologna. The two contributors to DeMi are:

•	Ekaterina Krasnova,

•	Mohammad Javad Farokhi Darani.

DeMi aims to study and analyze migration trends and demographics in Italy, focusing on two primary research questions:

•	What are the main countries of origin of immigrants in Italy, and how have these trends evolved over the last five years?

•	What are the demographic profiles of immigrants in Italy, including age, gender, and education level?

The background of this project stems from the increasing significance of migration as a global and local phenomenon, particularly within Italy. Migration impacts various aspects of society, such as labor markets, education, and public policy. The idea behind DeMi is to harness open datasets and digital tools to analyze migration trends, offering insights that enhance understanding of migration dynamics and guide policymaking.

To achieve its objectives, DeMi utilizes a collection of open datasets that have been analyzed from legal, ethical, and technical perspectives. The datasets were processed to create mashed-up data compliant with the principles of Linked Open Data, incorporating RDF models aligned with the [DCAT-AP](https://www.w3.org/TR/vocab-dcat-3/) ontology. This approach enabled the generation of high-quality, [5-star Linked Open Data](https://www.w3.org/community/webize/2014/01/17/what-is-5-star-linked-data/), which is freely downloadable and reusable.

The results of this project are presented through an interactive and user-friendly website, supported by clear documentation. Additionally, all scripts and derived datasets are shared on the project's GitHub repository under an open license, ensuring that the research is transparent, repeatable, and accessible to a broad audience.

# 2.	Scenario

DeMi seeks to provide valuable insights into the trends and profiles of immigrants in Italy, helping to address knowledge gaps and promote informed decision-making. By examining the main countries of origin of immigrants, along with their demographic profiles, our research aims to highlight patterns that are often underrepresented or misunderstood.

The information provided by DeMi holds immense value for a diverse range of individuals and groups. Researchers can use our findings to deepen their understanding of migration trends, uncovering patterns that inform studies on demographics, education, and labor markets. Policymakers, in turn, can rely on this data to craft targeted strategies for social integration, allocate resources more effectively, and design initiatives that address the needs of immigrant populations. Educators may find the demographic and educational insights particularly useful for shaping curricula and support programs that cater to students from diverse cultural and educational backgrounds. Similarly, community leaders and advocacy groups can leverage the data to develop initiatives like language workshops or mentorship programs, ensuring immigrants have the tools they need to integrate. Journalists and activists can use our research to challenge stereotypes and foster a more nuanced understanding of migration in public discourse.

However, despite its broad utility, the project encountered significant challenges. A notable issue was the lack of recent updates in many datasets, with some containing no new data since 2012. This presented difficulties in ensuring that our analysis was as accurate and comprehensive as possible.

Through these efforts, DeMi aims to empower a wide range of stakeholders by providing open, accessible, and reliable data. By presenting migration trends and insights in an understandable and meaningful way, our project contributes to a more informed and empathetic discourse on migration, supporting the development of more inclusive societies.

# 3.	Original dataset and mashed-up dataset

### 3.1. Original datasets
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

| ID  | Dataset link | Name | Unit of measure
| ------------- | ------------- | ------------- | ------------- |
| D13  | [data-explorer.oecd.org](https://data-explorer.oecd.org/vis?lc=en&fs%5B0%5D=Topic%2C1%7CSociety%23SOC%23%7CMigration%23SOC_MIG%23&pg=0&fc=Topic&bp=true&snb=6&vw=ov&df%5Bds%5D=dsDisseminateFinalDMZ&df%5Bid%5D=DSD_MIG%40DF_MIG&df%5Bag%5D=OECD.ELS.IMD&df%5Bvs%5D=1.0&dq=ITA..A.B11....&pd=2019%2C&to%5BTIME_PERIOD%5D=false&ly%5Bcl%5D=TIME_PERIOD&ly%5Brs%5D=SEX&ly%5Brw%5D=CITIZENSHIP)  | `OECD.ELS.IMD,DSD_MIG@DF_MIG,1.0+ITA..A.B11`; International migration database, Inflows of foreign population; Reference Area: Italy | Persons |
| D14  | [data-explorer.oecd.org](https://data-explorer.oecd.org/vis?lc=en&fs%5B0%5D=Topic%2C1%7CSociety%23SOC%23%7CMigration%23SOC_MIG%23&pg=0&fc=Topic&bp=true&snb=6&df%5Bds%5D=dsDisseminateFinalDMZ&df%5Bid%5D=DSD_MIG_INT%40DF_MIG_INT_TEMP&df%5Bag%5D=OECD.ELS.IMD&df%5Bvs%5D=1.0&dq=.A...&lom=LASTNPERIODS&lo=10&to%5BTIME_PERIOD%5D=false&vw=tb)  | `OECD.ELS.IMD,DSD_MIG_INT@DF_MIG_INT_TEMP,1.0+.A`; Standardised inflows of temporary migrants, Migration flows by category | Persons |
| D15  | [data-explorer.oecd.org](https://data-explorer.oecd.org/vis?df%5Bds%5D=dsDisseminateFinalDMZ&df%5Bid%5D=DSD_MIG_INT%40DF_MIG_INT_PER&df%5Bag%5D=OECD.ELS.IMD&df%5Bvs%5D=1.0&dq=.A...&lom=LASTNPERIODS&lo=10&to%5BTIME_PERIOD%5D=false)  | `OECD.ELS.IMD,DSD_MIG_INT@DF_MIG_INT_PER,1.0+.A`; Standardised inflows of permanent-type migrants, Migration flows by category | Persons |

### 3.2. Mashed-up dataset

!!! TO BE DONE !!!


# Quality analysis of the datasets
To conduct the quality analysis, we adhered to the [ISO/IEC 25012 standard](https://iso25000.com/index.php/en/iso-25000-standards/iso-25012), which outlines 15 key data quality characteristics, as shown in the picture below. 

![Picture 1](https://github.com/user-attachments/assets/58a8f18e-d348-499f-9db5-b64ca6c3133f)

These characteristics are grouped into two main categories: Inherent Data Quality and System-Dependent Data Quality. For this analysis, we focused exclusively on *Inherent Data Quality*, as it pertains to the intrinsic properties of the data itself, independent of any specific system or context. This focus allows us to evaluate the dataset's accuracy, completeness, consistency, credibility, and currentness comprehensively.

During the analysis, we observed that several columns contained a significant proportion of missing values. To quantify this issue, we calculated the percentage of completeness for each dataset using a [specialized algorithm](https://github.com/mjavadf/DeMi/blob/main/datasets/completeness.py), created with python. The detailed results of this evaluation are provided below.

**D1 - Italy, regions, provinces (IT1,29_7_DF_DCIS_POPSTRRES1_1,1.0):**

| **Characteristic** | **Description**                                   | **Findings**                                                                                           |
|---------------------|---------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| **Accuracy**        |     |       |
| **Completeness**    |     |   |
| **Consistency**     | |   |
| **Credibility**     |   | |
| **Currentness**     |  |                                                 |


**D2 - Italy, regions, provinces (IT1,29_316_DF_DCIS_POPSTRBIL1_1,1.0):**

| **Characteristic** | **Description**                                   | **Findings**                                                                                           |
|---------------------|---------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| **Accuracy**        |     |       |
| **Completeness**    |     |   |
| **Consistency**     | |   |
| **Credibility**     |   | |
| **Currentness**     |  |   


**D3 - Process and age class (IT1,29_849_DF_DCIS_ACQCITIZ_1,1.0):**

| **Characteristic** | **Description**                                   | **Findings**                                                                                           |
|---------------------|---------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| **Accuracy**        |     |       |
| **Completeness**    |     |   |
| **Consistency**     | |   |
| **Credibility**     |   | |
| **Currentness**     |  |   

**D4 - Immigrants - citizenship (IT1,28_185_DF_DCIS_MIGRAZIONI_2,1.0):**

| **Characteristic** | **Description**                                   | **Findings**                                                                                           |
|---------------------|---------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| **Accuracy**        | Data correctly represents real-world entities.    | CITIZENSHIP codes align with known conventions. Validation against ISO 3166 codes is recommended.     |
| **Completeness**    | All required data is present.                     | CITIZENSHIP has 31 missing values; OBS_STATUS and NOTE_* columns are mostly empty and should be evaluated for necessity. |
| **Consistency**     | Data is free from contradictions and uniform in format. | FREQ, SEX, and AGE columns show consistent formatting. A detailed review of value mappings (e.g., SEX values) would enhance understanding. |
| **Credibility**     | Data is trusted and reliable.                     | Appears credible based on structure, but external verification of data sources (e.g., DATAFLOW) is recommended. |
| **Currentness**     | Data is up-to-date.                               | TIME_PERIOD covers 2019–2023, reflecting recent data.                                                 |

**D5 - Type of residence permit and citizenship (IT1,29_348_DF_DCIS_PERMSOGG1_1,1.0):**

| **Characteristic** | **Description**                                   | **Findings**                                                                                           |
|---------------------|---------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| **Accuracy**        |     |       |
| **Completeness**    |     |   |
| **Consistency**     | |   |
| **Credibility**     |   | |
| **Currentness**     |  |   

**D6 - NI2024-Stranieri_altri_dati_2:**

| **Characteristic** | **Description**                                   | **Findings**                                                                                           |
|---------------------|---------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| **Accuracy**        |     |       |
| **Completeness**    |     |   |
| **Consistency**     | |   |
| **Credibility**     |   | |
| **Currentness**     |  |  

**D7 - DCCV_OCCUPATIT1_12012025111941696:**

| **Characteristic** | **Description**                                   | **Findings**                                                                                           |
|---------------------|---------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| **Accuracy**        |     |       |
| **Completeness**    |     |   |
| **Consistency**     |     |   |
| **Credibility**     |     |   |
| **Currentness**     |     |   |

**D8 - DCCV_OCCUPATIT1_12012025110421591:**

| **Characteristic** | **Description**                                   | **Findings**                                                                                           |
|---------------------|---------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| **Accuracy**        |     |       |
| **Completeness**    |     |   |
| **Consistency**     |     |   |
| **Credibility**     |     |   |
| **Currentness**     |     |   |

**D9 - DCCV_OCCUPATIT1_12012025110704049:**

| **Characteristic** | **Description**                                   | **Findings**                                                                                           |
|---------------------|---------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| **Accuracy**        |     |       |
| **Completeness**    |     |   |
| **Consistency**     |     |   |
| **Credibility**     |     |   |
| **Currentness**     |     |   |

**D10 - DCCV_TAXOCCU1_12012025110922125:**

| **Characteristic** | **Description**                                   | **Findings**                                                                                           |
|---------------------|---------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| **Accuracy**        |     |       |
| **Completeness**    |     |   |
| **Consistency**     |     |   |
| **Credibility**     |     |   |
| **Currentness**     |     |   |

**D11 - DCCV_TAXDISOCCU1_12012025111208359:**

| **Characteristic** | **Description**                                   | **Findings**                                                                                           |
|---------------------|---------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| **Accuracy**        |     |       |
| **Completeness**    |     |   |
| **Consistency**     |     |   |
| **Credibility**     |     |   |
| **Currentness**     |     |   |

**D12 - DCIS_PERMSOGG1_12012025111539693:**

| **Characteristic** | **Description**                                   | **Findings**                                                                                           |
|---------------------|---------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| **Accuracy**        |     |       |
| **Completeness**    |     |   |
| **Consistency**     |     |   |
| **Credibility**     |     |   |
| **Currentness**     |     |   |

**D13 - OECD.ELS.IMD,DSD_MIG@DF_MIG,1.0+ITA..A.B11:**

| **Characteristic** | **Description**                                   | **Findings**                                                                                           |
|---------------------|---------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| **Accuracy**        |     |       |
| **Completeness**    |     |   |
| **Consistency**     |     |   |
| **Credibility**     |     |   |
| **Currentness**     |     |   |

**D14 - OECD.ELS.IMD,DSD_MIG_INT@DF_MIG_INT_TEMP,1.0+.A:**

| **Characteristic** | **Description**                                   | **Findings**                                                                                           |
|---------------------|---------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| **Accuracy**        |     |       |
| **Completeness**    |     |   |
| **Consistency**     |     |   |
| **Credibility**     |     |   |
| **Currentness**     |     |   |

**D15 - OECD.ELS.IMD,DSD_MIG_INT@DF_MIG_INT_PER,1.0+.A:**

| **Characteristic** | **Description**                                   | **Findings**                                                                                           |
|---------------------|---------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| **Accuracy**        |     |       |
| **Completeness**    |     |   |
| **Consistency**     |     |   |
| **Credibility**     |     |   |
| **Currentness**     |     |   |

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

### Notes
- **D6** has a perfect completeness rate of 100%, with no null values detected.
- **D13** shows the highest completeness percentage at 93.30%.
- **D3**, **D4**, and **D5** have lower completeness percentages (around 47-48%), indicating that a significant portion of their data is missing.
- The completeness percentage varies widely across datasets, with values ranging from 47.62% to 100%. 
