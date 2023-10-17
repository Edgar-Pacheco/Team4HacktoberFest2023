# Proyecto Hacktoberfest 2023: Construcción de pipelines ETL con Código Abierto

## Tema

Pipeline de Extracción, Transformación y Carga (ETL) de Proteomas y Caracteristicas Clinicas de casos con Cáncer de Mama diagnosticado, con un componente de aprendizaje automático (ML) para realizar una detección oportuna y brindar las condiciones más adecuadas (medicacion, cuidados, etc.) para el paciente.

## Descripción 

La idea a desarrollar, es generar una aplicación FastAPI con integración de componenente de Machine Learning, la cual se alimenta con datos de Proteomas y Caracteristicas Clinicas de casos de Cáncer de Mama previamente diagnosticados y siendo estos positivos, para poder asi realizar una detección oportuna, y poder brindarle al paciente las condiciones mas adecuadas en cuanto a calidad de vida, farmacos, y cuidados, por mencionar algunos; finalmente, proporcionar la API al sector de la población que se encuentra inmersa en el tema para darles una mano de ayuda.

Se utilizaran 2 DataSets, los dos con licencias abiertas, uno que contiene Proteomas de 77 pacientes y el otro unicamente con caracteristicas clínicas, incluyendo datos de control negativo (pacientes sanos) para poder discernir y entender los datos de mejor manera.

La API se generara mediante Scripts de Python: extracción automatizada, generación de graficos para exploración de los datos (tablas y HeatMaps), junto con las PipeLines necesarias; se utiliza la paqueteria de DuckDB para crear una base de datos y manejar los mismos de una forma mas maleable y sencilla, y la paqueteria SeaBorn para la generación de HeatMaps.

El goal de nuestro proyecto es poder desplegar la API y que llegue al público objetivo, probarla con otros datos distintos a los utilizados para la generación de nuestro proyecto y poder hacer el 'double check' positivo; a futuro, podriamos tomar este proyecto como template y extrapolarlo a otros casos clinicos, para asi darle mas juego en todas las áreas que se pueda aplicar.

## Fuentes de Datos

1. Breast Cancer Proteomes: Contiene 77 perfiles proteomicos (Expresión de Proteinas) en los casos de cáncer de mama previamente diagnosticados, obtenidos del Clinical Proteomic Tumor Analysis (NCI/NIH), con valores de expresión para ~12,000 proteinas en cada una de las muestras. Licencia Desconocida. (https://www.kaggle.com/datasets/piotrgrabo/breastcancerproteomes)

2. Breast Cancer Coimbra: Contiene las características clínicas de 64 pacientes con cáncer de mama y 52 controles sanos. Contiene 10 predictores cuantitativos, y una variable dependiente binaria, que indica presencia o ausencia de cáncer de mama. Los modelos de predicción basados en estos predictores, si son precisos, pueden utilizarse potencialmente como biomarcadores del cáncer de mama. Licencia atribuida a Creative Commons Attribution 4.0 International. (https://archive.ics.uci.edu/dataset/451/breast+cancer+coimbra)

## Métodos

Describa los métodos que está utilizando. Incluya una descripción de las herramientas que está utilizando.

Para analisis y exploración de los datos, proponemos lo siguiente:
* Realizar una visualización general de los 2 DataSets seleccionados de forma generalizada, mostrando la MetaData (ubicación de recolección de los datos, fecha, cantidad de datos, clasificaciones, etc.)
* En lo correspondiente al DataSet de los Proteomas, generar un HeatMap en el cual se pueda visualizar los niveles de expresión de los genes de forma sencilla y fácil de entender, con su respectiva explicación de puntos clave.
    * Utilizamos la paqueteria **SeaBorn**, que es para visualización de datos y dibujo de gráficos estadísticos atractivos e informativos, basada en matplotlib. De esta paqueteria obtendremos los HeatMaps.
    * Para el manejo eficaz de los datos, se utiliza **DuckDB**, lo cual permite poder exportar los datos que necesitamos a una base de datos, y de ahi trabajar con dicha DB.
* En lo correspondiente al DataSet de las Caracteristicas Clinicas, generar tablas donde se organicen de forma clara y entendible los datos que se presentan.

## Interfaz de Usuario

La idea final es crear una Aplicación FastAPI, la cual sea flexible y fácil de utilizar para las personas, que sea de facil acceso y efectiva para el proposito de su creación, sirviendo asi de ayuda para el diagnostico tradicional/estandar para hoy día.

## Miembros del Equipo

* Jesús Gerardo Ortiz Romero / [@j-gorm](https://github.com/j-gorm)
* Edgar Pacheco Castan / [@Edgar-Pacheco](https://github.com/Edgar-Pacheco)
* Diego Peñaloza / [@diegopenaloza](https://github.com/diegopenaloza)
