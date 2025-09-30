
# LEER LIBREOFFICE CALC.ODS 
import pandas as pd

# ESPECIFICAR ODF
print("\nLEER LIBREOFFICE DE CALC 'ventas.ods' -  engine='odf' \n")
df3 = pd.read_excel('ventas.ods', engine='odf')

print( df3.head())
