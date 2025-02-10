
<h1 align="center">PROYECTO - SISTEMA DE RECOMENDACION DE PELICULAS</h1>



![Screenshot_20241211-015047_Instagram](https://github.com/user-attachments/assets/c0d5bb4f-5627-46f5-8996-4b05a0ba7431)


## Descripción

El objetivo principal de este proyecto es desarrollar un MVP (Producto Mínimo Viable) que implemente un sistema de recomendación de películas. Para lograrlo, se utilizó el cálculo de similitud del coseno, obteniendo asi las 5 mejores recomendaciones por pelicula proporcionada. El desarrollo se llevó a cabo en Python utilizando librerías como Pandas, nltk, Scikit-Learn, entre otras.

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

## Proceso
El enfoque seguido fue el de un especialista en Ingeniería de Datos o Machine Learning. Las etapas principales incluyeron:

1. ETL (Extracción - Transformación - Carga) de datos crudos:  
Se trabajó con dos conjuntos de datos iniciales en formato CSV, los cuales se procesaron de manera independiente. Tras las transformaciones y reducciones necesarias, se generaron nuevos archivos en csv, optimizando así los recursos computacionales necesarios para el despliegue en Render.

2. Análisis Exploratorio de Datos (EDA):  
Se analizaron los datos ya procesados mediante gráficos y consultas. Eleccion de las columnas como overview, genres y belongs_to_collection para el sistema de recomendacion.

3. Creación de funciones para la API:  
Se desarrollaron 6 funciones principales:  

- def cantidad_filmaciones_mes( Mes ): Se ingresa un mes en idioma Español. Debe devolver la cantidad de películas que fueron estrenadas en el mes consultado en la totalidad del dataset.

- def cantidad_filmaciones_dia( Dia ): Se ingresa un día en idioma Español. Debe devolver la cantidad de películas que fueron estrenadas en día consultado en la totalidad del dataset.

- def score_titulo( titulo_de_la_filmación ): Se ingresa el título de una filmación esperando como respuesta el título, el año de estreno y el score.

- def votos_titulo( titulo_de_la_filmación ): Se ingresa el título de una filmación esperando como respuesta el título, la cantidad de votos y el valor promedio de las votaciones. 

- def get_actor( nombre_actor ): Se ingresa el nombre de un actor que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno. Además, la cantidad de películas que en las que ha participado y el promedio de retorno.

- def get_director( nombre_director ): Se ingresa el nombre de un director que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno. Además, devolvera el nombre de cada película con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma.

4. Desarrollo de la API:  
Se utilizó el framework FastAPI para implementar las funciones creadas.

5. Modelado del sistema de recomendación:  
Se aplicó la técnica TF-IDF para vectorizar los datos, asegurando una reducción adecuada para optimizar el rendimiento del modelo. La similitud del coseno fue elegida por su simplicidad y eficiencia durante la implementación.


## Datos y Fuentes

[Link de los Datasets](https://drive.google.com/drive/folders/1X_LdCoGTHJDbD28_dJTxaD4fVuQC9Wt5)

[Link a Render](https://proyecto-individual-henry-11.onrender.com/docs)

[Video Demostrativo de la Api](https://www.youtube.com/watch?v=ctjgmCjU-EY&t=2s)

## Resultados y Conclusiones

Sistema de Recomendacion De Peliculas Concluido identificando las peliculas mas similares

