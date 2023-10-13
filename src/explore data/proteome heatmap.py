#Script para generar un Mapa de Calor de la expresión de los genes en Proteomas de pacientes con Cáncer de Mama
    #Gráfico clave para visualizar como se realiza la expresión génica en casos positivos a Cáncer de Mama

'''
pip install numpy
pip install pandas
pip install seaborn
pip install matplotlib
pip install openpyxl
'''

import numpy as np
import pandas as pd
import seaborn as sns
import duckdb
from matplotlib import pyplot as plt

def save_to_duckdb(df, table_name, db_path):
    """Save dataframe to duckdb"""
    conn = duckdb.connect(db_path)
    conn.register('df', df)
    
    # Check if table already exists, if not, create it
    tables = conn.execute("SHOW TABLES").fetchall()
    if table_name not in [table[0] for table in tables]:
        conn.execute(f"CREATE TABLE {table_name} AS SELECT * FROM df")
    
    conn.close()

df = pd.read_csv("C:/Users/gerar/Downloads/Breast Cancer Proteomes/77_cancer_proteomes_CPTAC_itraq.csv") 
save_to_duckdb(df, "Cancer_Proteomes", "Proteomes.duckdb")