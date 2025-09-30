
# Ej CLASE 3

# Lee los archivos subidos a la carpeta virtual de trabajo
# Hay que abrir el indice de archivos en el panel de la izq
# y luego subir el archivo manualmente


import defusedxml
import odfpy as odf

import pandas as pd      # Importar la librería Pandas
print( pd.__version__)

print( odf.__version__)

# LEER CVS
# Usar el método read_csv de Pandas (pd) que recibe como argumento el archivo 
# csv y retorna un dataframe

df1 = pd.read_csv("ventas.csv")
print(f"Number of rows of df1: {len(df1)}")
print( df1.head() )


# LEER XLSX
# Usar el método de Pandas (pd) que recibe como argumento el archivo csv y 
# retorna un dataframe

df2 = pd.read_excel("ventas.xlsx")
print(f"Number of rows of df2: {len(df2)}")
print( df2.head() )


