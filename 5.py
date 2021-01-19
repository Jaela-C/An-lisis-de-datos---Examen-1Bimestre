from argparse import ArgumentParser
import requests
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from bson import json_util, ObjectId
import couchdb

URL = 'http://jaela:654321@localhost:5984'
print(URL)
try:
    response = requests.get(URL)
    if response.status_code == 200:
        print('CouchDB connection: Success')
    if response.status_code == 401:
        print('CouchDB connection: failed', response.json())
except requests.ConnectionError as e:
    raise e

server=couchdb.Server(URL)
HEADERS = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

CLIENT = MongoClient('mongodb://localhost:27017')

try:
    CLIENT.admin.command('ismaster')
    print('MongoDB connection: Success')
except ConnectionFailure as cf:
    print('MongoDB connection: failed', cf)

DBS = CLIENT.get_database('examen')
dbsCollection = DBS.datos

dbc = server['mario_kart'] 
for db in dbc:
    try:
        dbsCollection.insert_one(dbc[db])
        print('Dato guardado en mongoDB')
    except TypeError as t:
        print('current document raised error: {}'.format(t))
        SKIPPED.append(db)  # creating list of skipped documents for later analysis
        continue    # continue to next document
    except Exception as e:
        raise e
