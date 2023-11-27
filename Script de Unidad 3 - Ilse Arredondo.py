#Indicamos el directorio en el que vamos a trabajar
import os
os.chdir(r'C:\Users\ilse-\PROGA\UNIDAD 3 ACTIVIDAD 1')

#Importamos los paquetes que vamos a necesitar
import pandas as pd #paqueteria
import matplotlib.pyplot as plt #paqueteria

#Leemos el archivo a analizar
bosque = pd.read_csv('Bosque.csv', sep=';',index_col=0)
bosque.info()
bosque.head()

#Creamos una funcion que cree el histograma
def crear_histograma(variable,j,z):
    plt.figure(j)
    plt.hist(bosque[variable], 15, color=z, ec="black")
    plt.title(f"Histograma {variable}")
    plt.savefig(f"{variable}.jpg")
    plt.show()

variable=["Temperatura1","Humedad relativa1","Localidad"]
colores=["red","blue","yellow"]
j=1
z=0

for i in variable:
    crear_histograma(i,j,colores[z])
    j +=1
    z +=1
