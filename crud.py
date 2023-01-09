# views.py

# python manage.py
# python -m websockets ws://localhost:8000/
import pymongo
from connection import create_connection

client = create_connection()

db1 = client["tradeHistory_db"]
live_data = db1['live_data']

filter_output = {"InstrumentIdentifier" : "NIFTY 50"}
unique_output = "PriceChangePercentage"
x = []

def get_mongo_data(data):
    
    filter_data  = ''

    if data == 'filter':
        filter_data = live_data.find(filter_output).count()

    elif data == 'unique':
        filter_data = live_data.distinct(unique_output)

    elif data == 'gainer':
        result = live_data.find().sort([("PriceChangePercentage", pymongo.DESCENDING)]).limit(10)
        for i in result:
            x.append(i)
            print(x)

    elif data == 'loser':
        result2 = live_data.find().sort([("PriceChangePercentage", pymongo.ASCENDING)]).limit(10)
        for i in result2:
            print(i)

    else:
        filter_data = live_data.find()
        
    return filter_data

# 'PriceChangePercentage': 3.33
# 'LastTradePrice': 699.35
# 'Close': 676.8