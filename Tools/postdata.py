#Importamos la configuración
from Configuracion.configuration import collection

#POST
def insert_quote(country,speech,year):
    """
    Dados un country, speech y year, genera un nuevo documento en la colección

    Takes: country (país), speech y year (año)
    Returns: Mensaje de comprobación con los datos introducidos
    """
    quote = {"Country": country,
    "Speech": speech,
    "Year": year
    }
    collection.insert_one(quote)