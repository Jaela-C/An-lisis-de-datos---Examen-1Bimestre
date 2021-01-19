from argparse import ArgumentParser
import requests
import pymongo 
from pymongo.errors import ConnectionFailure
from bson import json_util, ObjectId
import couchdb
import dns

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

client = pymongo.MongoClient("mongodb+srv://esfot:esfot@cluster0.yai72.mongodb.net/examenMA?retryWrites=true&w=majority")
dbm = client.get_database('examenMA')
dbma = dbm.datosMA

try:
    client.admin.command('ismaster')
    print('MongoDB Atlas connection: Success')
except ConnectionFailure as cf:
    print('MongoDB Atlas connection: failed', cf)

dbc = server['mario_kart'] 

for db in dbc:
    try:
        dbma.insert_one(dbc[db])
        print('Dato guardado en mongoDB Atlas')
    except TypeError as t:
        print('current document raised error: {}'.format(t))
        SKIPPED.append(db)  # creating list of skipped documents for later analysis
        continue    # continue to next document
    except Exception as e:
        raise e
