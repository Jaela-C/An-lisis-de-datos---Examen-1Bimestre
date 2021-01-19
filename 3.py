from facebook_scraper import get_posts
from pymongo import MongoClient
import json
import time

#conexión a mongoDB
MONGO_HOST = 'mongodb://localhost/examen'

i = 1
for post in get_posts('automovil', pages = 100000, extra_info = True):
    print(i)
    i += 1
    time.sleep(5)
    
    id = post['post_id']
    doc = {}
     
    doc['id'] = id
    
    mydate = post['time']
    
    try:
        doc['texto'] = post['text']
        doc['date'] = mydate.timestamp()
        doc['likes'] = post['likes']
        doc['comments'] = post['comments']
        try:
            doc['reactions'] = post['reactions']
        except:
            doc['reactions'] = {}

        doc['post_url'] = post['post_url']
        client = MongoClient(MONGO_HOST)
        db = client.examen
        print(doc)
        print("Dato de facebook guardado")
        db.datos.insert_one(doc)
        
    except Exception as e:    
        print("No se pudo guardar el dato:" + str(e))