# manage.py

# python manage.py

# python manage.py runserver
import asyncio
import websockets

from crud import get_mongo_data


# create handler for each connection

async def handler(websocket, path):
    try:
        data = await websocket.recv()
        res = get_mongo_data(data)
        for doc in res:
            print(doc)
        reply = f'reply is : {res}'
        await websocket.send(reply)
    except Exception as e:
        print(e) 


start_server = websockets.serve(handler, "localhost", 8000)
 
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()