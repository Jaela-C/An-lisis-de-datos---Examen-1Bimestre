from argparse import ArgumentParser
import requests
import pymongo 
from pymongo.errors import ConnectionFailure
from bson import json_util, ObjectId
import couchdb
import dns
import json

CLIENT = pymongo.MongoClient('mongodb://localhost:27017')

try:
    CLIENT.admin.command('ismaster')
    print('MongoDB connection: Success')
except ConnectionFailure as cf:
    print('MongoDB connection: failed', cf)

DBS = ['examen']

client = pymongo.MongoClient("mongodb+srv://esfot:esfot@cluster0.yai72.mongodb.net/examenMA?retryWrites=true&w=majority")
dbm = client.get_database('examenMA')
dbma = dbm.datosMA

try:
    client.admin.command('ismaster')
    print('MongoDB Atlas connection: Success')
except ConnectionFailure as cf:
    print('MongoDB Atlas connection: failed', cf)


for db in DBS:
    if db not in ('admin', 'local','config'):  
        cols = CLIENT[db].list_collection_names()  
        for col in cols:
            print('Querying documents from collection {} in database {}'.format(col, db))
            for x in CLIENT[db][col].find():  
                try:
                    documents = json.loads(json_util.dumps(x))
                    dbma.insert_one(documents)
                    print('Dato guardado en mongoDB Atlas')
                except:
                    print('El dato ya existe')