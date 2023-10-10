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
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\gerar\Downloads\77_cancer_proteomes_CPTAC_itraq.csv") #cambiar el path, esta linkeado a mi PC
print(df.head(79))

gene = ((np.asarray(df['gene_symbol'])).reshape(110,110))
expression = ((np.asarray(df['AO-A12D.01TCGA'])).reshape(110,110))
print(gene)
print(expression)

result = df.pivot(index='RefSeq_accession_number', columns='gene_symbol', values='AO-A12D.01TCGA')
print(result)

labels = (np.asarray(["{0} \n {1:.2f}".format(symb,value)
                      for symb, value in zip(gene.flatten(),
                                               expression.flatten())])
         ).reshape(110,110)

fig, ax = plt.subplots(figsize=(13,7))

title = "Breast Cancer Proteome Heat Map"

plt.title(title,fontsize=18)
ttl = ax.title
ttl.set_position([0.5,1.05])

ax.set_xticks([])
ax.set_yticks([])

ax.axis('off')

sns.heatmap(result,annot=labels,fmt="",cmap='RdYlGn',linewidths=0.10,ax=ax)
plt.show() #Error en la formulación del HeatMap, 'unable to allocate 895 MiB'