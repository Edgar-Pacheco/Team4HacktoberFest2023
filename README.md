# Hacktoberfest 2023 project: building ETL and RAG pipelines with open source 

## Set up /  Configuración

There should be one GitHub repository per team. /  Debería haber un repositorio de GitHub por equipo.

**Ensure all team members have completed all steps in the [set up](setup.md) document.**

**Asegúrate de que todos los miembros del equipo hayan completado todos los pasos en el [documento de configuración](setup-espanol.md).**

## Tema del Proyecto

Pipeline de Extracción, Transformación y Carga (ETL) de Proteomas y Caracteristicas Clinicas de casos con Cáncer de Mama diagnosticado, con un componente de aprendizaje automático (ML) para realizar una detección oportuna y brindar las condiciones más adecuadas (medicacion, cuidados, etc.) para el paciente.

## Description / Descripción 

Proporcione una descripción de su proyecto. Incluya las fuentes de datos que está utilizando, las herramientas que está utilizando y el resultado esperado de su proyecto.

## Data sources / Fuentes de datos

Se utilizaran 2 datasets, provenientes de distintas fuentes.

DS 1: Breast Cancer Proteomes. Contiene 77 perfiles proteomicos (Expresión de Proteinas) en los casos de cáncer de mama previamente diagnosticados, obtenidos del Clinical Proteomic Tumor Analysis (NCI/NIH), con valores de expresión para ~12,000 proteinas en cada una de las muestras. Licencia Desconocida. (https://www.kaggle.com/datasets/piotrgrabo/breastcancerproteomes)

DS 2: Breast Cancer Coimbra. Contiene las características clínicas de 64 pacientes con cáncer de mama y 52 controles sanos. Contiene 10 predictores cuantitativos, y una variable dependiente binaria, que indica presencia o ausencia de cáncer de mama. Los modelos de predicción basados en estos predictores, si son precisos, pueden utilizarse potencialmente como biomarcadores del cáncer de mama. Licencia atribuida a Creative Commons Attribution 4.0 International. (https://archive.ics.uci.edu/dataset/451/breast+cancer+coimbra)

## Methods / Métodos

Describa los métodos que está utilizando. Incluya una descripción de las herramientas que está utilizando.

## User interface your project will have / Interfaz de usuario que tendrá su proyecto

Describa la interfaz de usuario que tendrá su proyecto. Incluya una descripción de las herramientas que está utilizando.

Opciones:

1. Aplicación FastAPI
2. Aplicación Chainlit
3. Tablero Voila

## Team members/ Miembros del equipo

Agregue los nombres y las ID de GitHub de los miembros de su equipo aquí.

Jesús Gerardo Ortiz Romero / @j-gorm
