# settings.py

import pymongo

def create_connection():
    try:
        client = pymongo.MongoClient("mongodb+srv://naveen:Naveen#123@cluster0.evdmoau.mongodb.net/?retryWrites=true&w=majority")
        print('connection created successfully!!!')
        return client
    except Exception as e:
        print('Error occured: ', e)