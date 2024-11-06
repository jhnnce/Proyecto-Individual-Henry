

## Descripción

Este proyecto tiene como objetivo analizar datos de películas, identificar patrones de relación para un sistema de recomendación usando técnicas de ciencia de datos.

## Tabla de contenido

Introducción  
Instalación y Requisitos  
Estructura del Proyecto  
Datos y Fuentes  
Metodología  
Resultados y Conclusiones  

## Instalación y Requisitos
Requisitos:  

Python 3.7 o superior  
pandas  
numpy  
matplotlib  
scikit-learn  
Nltk  
Fastapi  
Os  
Datetime  
Matplotlib  
Seaborn  
Nltk  
Json  
TfidfVectorizer  
cosine_similarity  
Ast  
json  

## Estructura del Proyecto

Dataset/: Dataset del proyecto  
Notebook/: Jupyter notebooks con el análisis.  
main.py: Código fuente.  
Requirements.txt: Librerias necesarias para el proyecto.  
README.md: Documentación.  

## Uso y Ejecución  

Ejecutar EDA.ipynb en notebooks/ para análisis.  
Ejecutar main.py para generar el sistema de recomendación.  

## Datos y Fuentes

Link directo a los datasets: https://drive.google.com/drive/folders/1X_LdCoGTHJDbD28_dJTxaD4fVuQC9Wt5

## Metodología

Se aplicaron modelos de recomendación como la similitud del coseno, librerías que vectorizan palabras y proporcionan listas de stopwords como TfidfVectorizer y estemizadores para obtener la raíz de las palabras.

Se identificaron columnas relevantes para el sistema de recomendación como: belongs_to_collection, genres y overview que propocionan informacion suficiente para este fin.

Al realizar el filtro o reduccion del dataset por cantidad de votos ordenados de mayor a menor, se dejo de la lado usar estas mismas columnas como vote_average (promedio de votos) y vote_count (cantidad de votos ) para el sistema de recomendación, ademas para este caso, estas columnas podrían alterar los resultados ya que el algoritmo podría terminar recomendando por popularidad antes que por similitud.

## Resultados y Conclusiones

Sistema de Recomendacion De Peliculas Concluido identificando las peliculas mas similares

