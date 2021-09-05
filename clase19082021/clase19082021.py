# 1.	Overall Rank= Posición a nivel mundial
# 2.	Country or región= País
# 3.	hapiness_Score= Puntuación de felicidad (entre más grande mayor felicidad) 
# 4.	GDP per capita= PIB per cápita
# 5.	Social support=Apoyo social
# 6.	Healthy life expectancy= Esperanza de vida
# 7.	Freedom to make life choices= Libertad
# 8.	Generosity= Generosidad
# 9.	Perceptions of corruption= Percepción de la corrupción
import pandas as pd
import seaborn as sns
import numpy as np 
import missingno as msno
import matplotlib.pyplot as plt
import seaborn as sns
#%% Cargar datos
#Create a data frame with pandas
data = pd.read_csv('2020_report.csv')
#Show general info
data.info()
#Tenemos 138 observaciones, 10 columnas
#Continent and country son variables cualitativas
#Todas las columnas tienen valores (138) no hay faltantes
print(data.columns)

# Missing values: Diagrama de barras
plt.figure()
msno.bar(data)
plt.show()

# =============================================================================
# # Example dataframe.iloc With slice objects.
# # df
# #       a     b     c     d
# # 0     1     2     3     4
# # 1   100   200   300   400
# # 2  1000  2000  3000  4000
# 
# # df.iloc[1:3, 0:3]
# #       a     b     c
# # 1   100   200   300
# # 2  1000  2000  3000
# =============================================================================

#Extraer Solamente variables cuantitativas
#Get all rows from column 1-8 (9-1)
data1=data.iloc[:,1:9]

#Calcular la media
media=data1.mean()
print(media)
#Ejemplo de la media de una sola variable
print(f"La media de la happiness score es {data1['happiness_score'].mean()}")

#Graficar la media de media[0] (happiness_score)
plt.figure()
print(np.arange(138))
#Gráfico de dispersión or scatter
plt.scatter(np.arange(138), data1['happiness_score'])
#Generate a line in a matrix of ones in media point
print(np.ones(138))
print(media[0] * np.ones(138))
#graficar linealmente
plt.plot(np.arange(138), media[0] * np.ones(138), c='r')
plt.xlabel("Overall Rank")
plt.ylabel("Hapiness Score")
plt.show()

# #Calcular la mediana
mediana=data1.median()
print(mediana)

#Graficar la mediana
plt.figure()
plt.scatter(np.arange(138), data1['happiness_score'])
plt.plot(np.arange(138), mediana[0] * np.ones(138), c='r')
plt.xlabel("Overall Rank")
plt.ylabel("Hapiness Score")
plt.show()

#Calcular la moda
moda=data1.mode()
print(moda)

# #Graficar la moda
# plt.figure()
# plt.scatter(np.arange(138), data1['happiness_score'])
# plt.plot(np.arange(138), moda.iloc[0,0] * np.ones(138), c='r')
# plt.xlabel("Overall Rank")
# plt.ylabel("Hapiness Score")
# plt.show()

# plt.plot(np.arange(138),data1['happiness_score'].median()*np.ones(138), c='r')
# plt.plot(np.arange(138),data1['happiness_score'].mean()*np.ones(138), c='y')
# plt.plot(np.arange(138),data1['happiness_score'].mode()*np.ones(138), c='b')