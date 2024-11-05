from fastapi import FastAPI
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.metrics.pairwise import cosine_similarity
import re 
from nltk.stem.porter import PorterStemmer
import locale
import numpy as np
import os
import sqlite3

app = FastAPI()


df_movies = pd.read_csv('Dataset/df_movies.csv', sep=',') #leemos el dataset 
df_movies.release_date = df_movies.release_date.apply(pd.to_datetime) #transformamos la columna release_date en formato datetime
df_movies.dropna(inplace=True) # eliminamos datos faltantes en caso las haya
df_movies=df_movies.reset_index(drop=True) # reseteamos el indice del dataframe

# VARIABLES PARA EL SISTEMA DE RECOMENDACION


@app.get('/cantidad_filmaciones_mes')
async def cantidad_filmaciones_mes(mes: str):
    '''Devuelve la cantidad de películas estrenadas en un determinado mes
    
    Args:
        mes (str): Nombre del mes en español

    Returns:
        str (valido) : La cantidad de películas que fueron estrenadas en el mes
        str (invalido) : Respuesta que indica que se ingresó un mes incorrecto
    '''
    #locale.setlocale(locale.LC_TIME, 'es_ES') # cambiamos la configuracion a local - español
    # Diccionario de meses en español a inglés
    meses_espanol = {
        "enero": "January",
        "febrero": "February",
        "marzo": "March",
        "abril": "April",
        "mayo": "May",
        "junio": "June",
        "julio": "July",
        "agosto": "August",
        "septiembre": "September",
        "octubre": "October",
        "noviembre": "November",
        "diciembre": "December"
    }

    # Normalizar el mes ingresado
    mes_normalizado = mes.lower()

    # Verificar si el mes ingresado es válido
    if mes_normalizado not in meses_espanol:
        return {'message': 'Ingreso un mes incorrecto'}

    n = 0
    for fecha in df_movies.release_date:# Iteramos la columna
        if fecha.strftime('%B').lower() == meses_espanol[mes_normalizado].lower(): # Comparamos
            n += 1 # Sumamos si coincide

    return {"message": f"{n} cantidad de películas fueron estrenadas en el mes de {mes.capitalize()}!"}


@app.get('/cantidad_filmaciones_dia')
async def cantidad_filmaciones_dia(dia: str):
    '''Devuelve la cantidad de películas estrenadas en un determinado día
    
    Args:
        dia (str): Nombre del día en español

    Returns:
        str (valido) : La cantidad de películas que fueron estrenadas en ese día
        str (invalido) : Respuesta que indica que se ingresó un día incorrecto
    '''
    #locale.setlocale(locale.LC_TIME, 'es_ES') # cambiamos la configuracion a local - español
    # Diccionario de días en español a inglés
    dias_espanol = {
        "lunes": "Monday",
        "martes": "Tuesday",
        "miércoles": "Wednesday",
        "jueves": "Thursday",
        "viernes": "Friday",
        "sábado": "Saturday",
        "domingo": "Sunday"
    }

    # Normalizar el día ingresado
    dia_normalizado = dia.lower()

    # Verificar si el día ingresado es válido
    if dia_normalizado not in dias_espanol:
        return {'message': 'Ingreso un día incorrecto'}

    n = 0
    for fecha in df_movies.release_date:  # Iteramos la columna
        if fecha.strftime('%A').lower() == dias_espanol[dia_normalizado].lower():  # Comparamos
            n += 1  # Sumamos si coincide

    return {"message": f"{n} cantidad de películas fueron estrenadas en el día {dia.capitalize()}!"}


@app.get('/titulo_de_la_filmación')
async def score_titulo(titulo_de_la_filmación: str):
    '''Devuelve informacion como año de estreno y la popularidad de una pelicula
    
    Args:

        titulo_de_la_filmación (str): Nombre de la pelicula

    Returns:

        str (valido) : La película {titulo_de_la_filmación} fue estrenada en el año {year} con un score/popularidad de {score}
        str (invalido) : 'La pelicula {titulo_de_la_filmación} no existe'
    
    '''
    n=0 

    for i in range(len(df_movies.title)):
        
        if df_movies.title[i].lower() == titulo_de_la_filmación.lower(): #obtenemos el dia en español y lo comparamos con el valor ingresado
    
            
            lista_score = df_movies.loc[i,['title', 'release_year', 'popularity']].values # filtramos las columnas y posteriomente extraemos los valores
            movie = lista_score[0]
            year = lista_score[1]
            score = lista_score[2]
            n+=1 # definimos una variable que se sumara una unidad en cada iteracion dentro de la condicion
            return {'message':f'La película {movie} fue estrenada en el año {year} con un score/popularidad de {score}'}
        
        else:
            pass
    
    if n==0:
        return {'message':f'La pelicula {titulo_de_la_filmación} no existe'}

    else:
        pass
@app.get('/titulo_de_la_filmación_votos')
async def votos_titulo(titulo_de_la_filmación: str):

    '''Devuelve la pelicula, el año de estreno, la cantidad de votos y el promedio de votos.
    
    Args:

        titulo_de_la_filmación_votos (str): titulo de la filmacion

    Returns:

        str (valido) : La película {movie} fue estrenada en el año {year}. La misma cuenta con un total de {vote_count} valoraciones, con un promedio de {vote_average}
        str (invalido) : La pelicula {titulo_de_la_filmación} no cumple con esta condicion
    
    '''

    n=0 

    for i in range(len(df_movies.title)):
        
        if df_movies.title[i].lower() == titulo_de_la_filmación.lower() and df_movies.vote_count[i] >= 2000: # definimos la condicion 
    
            
            lista_vote = df_movies.loc[i,['title', 'release_year','vote_count','vote_average']].values # filtramos las columnas y posteriomente extraemos los valores
            movie = lista_vote[0]
            year = lista_vote[1]
            vote_count = lista_vote[2]
            vote_average = lista_vote[3]

            n+=1 # definimos una variable que se sumara una unidad en cada iteracion dentro de la condicion
            return {'message':f'La película {movie} fue estrenada en el año {year}. La misma cuenta con un total de {vote_count} valoraciones, con un promedio de {vote_average}'}
        
        else:
            pass
    
    if n==0:
        return {'message':f'La pelicula {titulo_de_la_filmación} no cumple con esta condicion'}

    else:
        pass
@app.get('/nombre_actor')
async def get_actor(nombre_actor: str):

    '''Devuelve el nombre del actor, la cantidad de peliculas en las que participo, el retorno total y el promedio del retorno.
    
    Args:

        nombre_actor (str): Nombre del actor

    Returns:

        str (valido) : El actor {nombre_actor} ha participado de {peliculas} cantidad de filmaciones, el mismo ha conseguido un retorno de {retorno} con un promedio de {retorno/peliculas} por filmación
        str (invalido) : El nombre del actor {nombre_actor} no existe
    
    '''

    peliculas=0
    retorno=0
    
    for i in range(len(df_movies.Actors)): # iteramos al tamaño de la columna
        if nombre_actor.lower() in df_movies.Actors[i].lower(): # si el nombre del actor se encuentra en la fila como condicion
            
            lista_actors = df_movies.loc[i,['Actors', 'return']].values # filtramos las columnas y posteriomente extraemos los valores
            peliculas+=1 # definimos una variable que se sumara una unidad en cada iteracion dentro de la condicion
            
            retorno += lista_actors[1] # definimos una variable que se sumara el valor del retorno en cada iteracion
        
        else:
            pass

    if peliculas==0: # definimos una condicion en caso no exista peliculas
            
    
        return {'message':f'El nombre del actor {nombre_actor} no existe'}

    else:
        return {'message':f'El actor {nombre_actor.capitalize()} ha participado de {peliculas} cantidad de filmaciones, el mismo ha conseguido un retorno de {retorno} con un promedio de {retorno/peliculas} por filmación'}


@app.get('/nombre_director')    
def get_director(nombre_director: str):

    '''Devuelve el nombre del director, las peliculas en que participo asi como su correspondiente año de estreno, inversion, ganancia y retorno de cada pelicula, tambien devuelve la cantidad total de peliculas y el retorno total.
    
    Args:

        nombre_director (str): Nombre del director

    Returns:

        str (valido) : El director {nombre_director} ha participado en:\n{peliculas} peliculas, el mismo ha conseguido un retorno total de {retorno_total}
        str (invalido) : El nombre del director {nombre_director} no existe
    
    '''

    peliculas=0
    retorno_total=0
    mj = ''
    
    for i in range(len(df_movies.Directores)): # iteramos la cantidad de filas de la columna
        if nombre_director.lower() in df_movies.Directores[i].lower(): # si el nombre del director se encuentra en la fila, como condicion
            
            lista_directors = df_movies.loc[i,['title', 'release_date','return', 'budget', 'revenue']].values # filtramos las columnas y posteriomente extraemos los valores
            
            title = lista_directors[0]
            release_date = lista_directors[1]
            retorno = lista_directors[2]
            revenue = lista_directors[3]

            peliculas+=1 # definimos una variable que se sumara una unidad en cada iteracion dentro de la condicion
            
            retorno_total += retorno # definimos una variable que se sumara el valor del retorno en cada iteracion

            mj += f'\n{title}, estrenada en {release_date}, el mismo ha conseguido un retorno de {retorno} y una ganancia de {revenue}' #en cada iteracion concatenamos el siguiente string

            
        
        else:
            pass

    if peliculas==0: # definimos una condicion en caso no exista peliculas
            
    
        return {'message':f'El nombre del director {nombre_director} no existe'}

    else:
        return {'message':f'El director {nombre_director.capitalize()} ha participado en:\n{mj}\n\nEl director {nombre_director.capitalize()} ha participado en:\n{peliculas} peliculas, el mismo ha conseguido un retorno total de {retorno_total}'}





@app.get('/recomendacion') 
def recomendacion(titulo: str):

    similarity_matrix_df = pd.read_csv('Dataset/similarity_matrix_df.csv', sep=',')
    
    movie = df_movies[df_movies['title'].str.lower() == titulo.lower()]

    if not movie.empty:
        movie_index = movie.index[0] #obtenemos el indice
        movie_similarities = similarity_matrix_df.iloc[movie_index,:] # obtenemos la fila que contiene los valores de similitud entre todas las peliculas y la pelicula especificada 
        most_similar_movie_indices = np.argsort(-movie_similarities) # ordenamos los indices de forma descendente
        most_similar_movie = df_movies.loc[most_similar_movie_indices, 'title'] # buscamos todas las peliculas similares con respecto a los indices de las peliculas en el dataset original
        
        return {'message':f'Las peliculas más similares al titulo", {titulo}, "son:\n{most_similar_movie[:10]}'}
        
    else:
        return {'message':f'La pelicula {titulo}, No existe'}
