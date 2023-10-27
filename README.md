# Hacktoberfest 2023 Project: Generation of a Report using Voila Dashboard.

## Theme

<img align="right" width="215" height="373" src="https://static.vecteezy.com/system/resources/previews/023/485/558/original/breast-cancer-pink-ribbon-png.png">Generation of a <strong>report</strong> with <strong>proteomic profile data</strong>, i.e., <strong>protein expression</strong>, of <strong>77 patients diagnosed with <em>breast cancer</em></strong>, for a better understanding of how gene expression behaves in positive cases and to detect possible <strong>new molecular markers</strong> for <em>early</em> and <em>timely</em> detection, through Voila Dashboards.

## Description 

The approach we decided to take is mostly an **exploratory analysis** of data, in this case, *biological* data pertinent to positive breast cancer cases, which were previously diagnosed. This analysis, with a good interpretation, could open doors to the identification of *__novel molecular markers__* that allow early identification of this clinical condition; in the future, this type of reports, already well established and with a previous research in scientific literature, we can deploy them in the cloud to share results and that all interested persons can have access, in addition, could be complemented with the help of _ETL processes_ for a more effective management of data and a more efficient and faster exploratory analysis. Only 1 Dataset was used, with open license, which contains Proteomes of 77 patients.

The report will be generated by means of a **Python** script in a **Jupyter Notebook**, which will upload the data to a database for efficient data management, in order to generate HeatMaps, which will show the level of expression of the proteins in each profile. The **DuckDB** package will be used to efficiently manage the data in a Database and the **SeaBorn** package will be used to generate HeatMaps.

The **goal** of the project is to be able to deploy the report online, so that it can be available to anyone who is interested in studying what was done and give play to future research.

## Data Sources

- **Breast Cancer Proteomes:** Contains 77 proteomic (Protein Expression) profiles on previously diagnosed breast cancer cases obtained from the Clinical Proteomic Tumor Analysis (NCI/NIH), with expression values for ~12,000 proteins in each of the samples. License Unknown. (https://www.kaggle.com/datasets/piotrgrabo/breastcancerproteomes)

## Methods

For the **analysis** and **exploration** of the data, the following is proposed:
* Generate a _HeatMap_ in which the gene expression levels can be visualized in a simple and easy to understand way, with their respective explanation of key points.
    * We use the **SeaBorn** package, which is for data visualization and drawing of attractive and informative statistical graphs, based on matplotlib. From this package we will obtain the HeatMaps.
    * For efficient data management, **DuckDB** is used, which allows us to export the data we need to a database, and from there work with that DB.

## User Interface

The final idea is to **deploy** the report through **Voila Dashboards**, to show the exploratory analysis online to anyone who is interested and to have a basis to continue generating reports in the future.

## Team Members

* __Jesús Gerardo Ortiz Romero / [@j-gorm](https://github.com/j-gorm)__: Generation of the Notebook with the exploratory analysis and deployment of the Report.
* __Edgar Pacheco Castan / [@Edgar-Pacheco](https://github.com/Edgar-Pacheco)__
* __Diego Peñaloza / [@diegopenaloza](https://github.com/diegopenaloza)__

## Final Product
<img align="right" width="405" height="289" src="https://github.com/ploomber/ploomber/blob/master/_static/logo.png?raw=true">Here is our <a href="https://github.com/ploomber/ploomber"><strong>final product!</strong></a>
Thanks a lot to <a href="https://github.com/ploomber/ploomber"><strong>Ploomber</strong></a> team and their mentoring programs, thanks to them we were able to deploy the reports online!