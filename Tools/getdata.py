#Importamos la configuración
from Configuracion.configuration import db,collection

#LISTAS
def list_UN():
    """
    Esta función te devuelve todo el dataset de UN General Debates

    Takes: nada
    Return: todo el dataset de UN General Debates
    """
    query = list(collection.find({}, {"_id":0}))
    return query

def list_year():
    """
    Esta función te devuelve una lista de todos los años medidos 

    Takes: nada
    Return: todas los años medidos
    """
    query = list(collection.distinct("Year"))
    return query

def list_country():
    """
    Esta función te devuelve una lista con todos los paises

    Takes: nada
    Return: todos los países
    """
    query = list(collection.distinct("Country"))
    return query

def list_speech():
    """
    Esta función te devuelve una lista con todos los speechs

    Takes: nada
    Return: todos los speechs
    """
    query = list(collection.distinct("Speech"))
    return query


#QUERIES DINÁMICAS/ LLAMADAS DEL USUARIO CON PARÁMETROS
def sentence_country(country):
    """
    Para un año país dado, está función te devuelve una lista con todos los speechs de ese país

    Takes: country (país)
    Return: todos los speechs de ese país
    """
    query = {"Country": country}
    proyeccion = {"_id":0}
    speech = list(collection.find(query,proyeccion))
    return speech

def sentence_year(year):
    """
    Para un año país dado, está función te devuelve una lista con todos los speechs de ese año

    Takes: year (año)
    Return: todos los speechs de ese año
    """
    query = {"Year": year}
    proyeccion = {"_id":0}
    speech = list(collection.find(query,proyeccion))
    return speech

def sentence_year_country(year,country):
    """
    Para un año país y año dado, está función te devuelve una lista con todos los speechs de ese país y año

    Takes: country (país), year (año)
    Return: todos los speechs de ese país y año
    """
    query = {"Year":year,"Country":country}
    proyeccion = {"_id":0}
    speech = list(collection.find(query,proyeccion))
    return speech