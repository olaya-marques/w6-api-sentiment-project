#1. Importación de librerias
import os
import dotenv
from pymongo import MongoClient

#2. Cargamos el dotenv en base a nuestro archivo .env
dotenv.load_dotenv()

dburl = os.getenv("URL")

#3. checkpoint de que tenemos correctamente el URL
print(dburl)
if not dburl:
    raise ValueError ("No tienes URL de mongodb")

#Nos conectamos con la base de datos
client = MongoClient(dburl)
db = client.get_database()
collection = db["frases"]