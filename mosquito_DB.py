# -*- coding: utf-8 -*-
import json
#import requests
from pymongo import MongoClient

#데이터 불러오기
file_path = '/Users/yunsu/seoul_mosquito_status_project/data/seoul_mosquito_status.json'
with open(file_path) as json_file:
    json_data = json.load(json_file)


##데이터베이스에 연결하기
HOST = 'cluster0.mmafh.mongodb.net'
USER = 'mosquitoUser'
PASSWORD = 'mosquito1234'
DATABASE_NAME = 'myFirstDatabase'
MONGO_URI = f"mongodb+srv://{USER}:{PASSWORD}@{HOST}/{DATABASE_NAME}?retryWrites=true&w=majority"

client = MongoClient(MONGO_URI)
database = client[DATABASE_NAME]

##table = collection
COLLECTION_NAME = 'mosquito_collection'
collection = database[COLLECTION_NAME]

#데이터 삽입
#반복해서 수행할 경우 같은 정보가 삽입된다.
collection.insert_one(json_data)