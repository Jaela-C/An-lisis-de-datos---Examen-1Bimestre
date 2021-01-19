import requests
from bs4 import BeautifulSoup
import pandas as pd
from pymongo import MongoClient
import json

#Encontrar cadena pequeña
def find_2nd(string, substring):
    return string.find(substring, string.find(substring) + 1) #Encuentra una cadena

#Encontrar cadena grande
def find_1st(string, substring):
    return string.find(substring, string.find(substring)) #Encuentra una cadena

response = requests.get('https://vehiculos.mercadolibre.com.ec/#c_id=/home/categories/element&c_category_id=MEC1743&c_uid=afa1da34-f7a8-4f19-adfc-b5699a4b56c1')
soup = BeautifulSoup(response.content, 'lxml')

Nombre_V = []
Localizacion_V = []
Precio_V = []

post_nombre = soup.find_all('h2', class_ = 'ui-search-item__title ui-search-item__group__element')
post_localizacion = soup.find_all('span', class_ = 'ui-search-item__group__element ui-search-item__location')
post_precio = soup.find_all('span', class_ = 'price-tag-fraction')

for element in post_nombre:
    element = str(element)
    limpio = str(element[find_1st(element, '>') + 1:find_2nd(element, '<')])
    Nombre_V.append(limpio.strip())

for element in post_localizacion:
    element = str(element)
    limpio = str(element[find_1st(element, '>') + 1:find_2nd(element, '<')])
    Localizacion_V.append(limpio.strip())

for element in post_precio:
    element = str(element)
    limpio = str(element[find_1st(element, '>') + 1:find_2nd(element, '<')])
    Precio_V.append(limpio.strip())

dfDS = pd.DataFrame({'Nombre Vehículo':Nombre_V, 'Localización Vehículo':Localizacion_V, 'Precio Vehículo':Precio_V})
result = dfDS.to_json(orient = "records")
parsed = json.loads(result)

#conexión a mongoDB
MONGO_HOST = 'mongodb://localhost/examen'

for post in parsed:
    try:
        client = MongoClient(MONGO_HOST)
        db = client.examen         
        db.datos.insert_one(post)
        print("Dato guardado en MongoDB")
    except Exception as e:    
        print("no se pudo grabar:" + str(e))