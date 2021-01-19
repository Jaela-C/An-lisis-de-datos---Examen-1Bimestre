import sqlite3
import pandas as pd
import json

con = sqlite3.connect("database.db")

dfsqlite = pd.read_sql_query("SELECT * FROM  transportes",con)

dfsqlite

result = dfsqlite.to_json(orient = "records")
parsed = json.loads(result)
json.dumps(parsed)

#conexión a mongoDB
MONGO_HOST = 'mongodb://localhost/examen'

for dato in parsed:
    try:
        client = MongoClient(MONGO_HOST)
        db = client.examen         
        db.datos.insert_one(dato)
        print("Dato guardado en MongoDB")
    except Exception as e:    
        print("no se pudo grabar:" + str(e))