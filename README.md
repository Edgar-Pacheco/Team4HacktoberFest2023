# Proyecto Hacktoberfest 2023: Construcción de pipelines ETL con Código Abierto

## Tema del Proyecto

Pipeline de Extracción, Transformación y Carga (ETL) de Proteomas y Caracteristicas Clinicas de casos con Cáncer de Mama diagnosticado, con un componente de aprendizaje automático (ML) para realizar una detección oportuna y brindar las condiciones más adecuadas (medicacion, cuidados, etc.) para el paciente.

## Descripción 

Proporcione una descripción de su proyecto. Incluya las fuentes de datos que está utilizando, las herramientas que está utilizando y el resultado esperado de su proyecto.

La idea a desarrollar, es generar una API con integración de ML con datos de Proteomas y Caracteristicas Clinicas de casos de Cáncer de Mama previamente diagnosticado para poder realizar una detección oportuna, para así brindarle al paciente las condiciones mas adecuadas en cuanto a calidad de vida, farmacos, y cuidados, por mencionar algunos, y proporcionarlo a la población que se encuentra inmersa en el tema para darles una mano de ayuda.
Se utilizaran 2 DataSets, los dos con licencias abiertas, uno que contiene Proteomas de 77 pacientes y el otro unicamente con caracteristicas clínicas, incluyendo datos de control negativo para poder discernir y entender los datos de mejor manera.
La API se generara mediante Scripts de Python, para extracción automatizada, generación de graficos para exploración de los datos, y las PipeLines necesarias, con la utilización de DuckDB para subir la información a una DB, y SeaBorn para la generación de HeatMaps.

## Fuentes de datos

Se utilizaran 2 datasets, provenientes de distintas fuentes.

1. Breast Cancer Proteomes: Contiene 77 perfiles proteomicos (Expresión de Proteinas) en los casos de cáncer de mama previamente diagnosticados, obtenidos del Clinical Proteomic Tumor Analysis (NCI/NIH), con valores de expresión para ~12,000 proteinas en cada una de las muestras. Licencia Desconocida. (https://www.kaggle.com/datasets/piotrgrabo/breastcancerproteomes)

2. Breast Cancer Coimbra: Contiene las características clínicas de 64 pacientes con cáncer de mama y 52 controles sanos. Contiene 10 predictores cuantitativos, y una variable dependiente binaria, que indica presencia o ausencia de cáncer de mama. Los modelos de predicción basados en estos predictores, si son precisos, pueden utilizarse potencialmente como biomarcadores del cáncer de mama. Licencia atribuida a Creative Commons Attribution 4.0 International. (https://archive.ics.uci.edu/dataset/451/breast+cancer+coimbra)

## Métodos

Describa los métodos que está utilizando. Incluya una descripción de las herramientas que está utilizando.

Para analizar los datos, proponemos lo siguiente:
* Realizar una visualización general de los 2 DataSets seleccionados de forma generalizada, mostrando la MetaData (ubicación de recolección de los datos, fecha, cantidad de datos, clasificaciones, etc.)
* En lo correspondiente al DataSet de los Proteomas, generar un HeatMap en el cual se pueda visualizar los niveles de expresión de los genes de forma sencilla y fácil de entender, con su respectiva explicación de puntos clave.
    *Se utilizara la paqueteria SeaBorn para generar el HeatMap.
* En lo correspondiente al DataSet de las Caracteristicas Clinicas, generar tablas donde se organicen de forma clara y entendible los datos que se presentan.

## Interfaz de usuario que tendrá su proyecto

Sera una Aplicación FastAPI.

## Miembros del equipo

Jesús Gerardo Ortiz Romero / [@j-gorm](https://github.com/j-gorm)
Edgar Pacheco Castan / [@Edgar-Pacheco](https://github.com/Edgar-Pacheco)
Diego Peñaloza / [@diegopenaloza](https://github.com/diegopenaloza)
