import requests
import asyncio
import json

from azure.eventhub import EventData
from azure.eventhub.aio import EventHubProducerClient
 
subreddit = 'dataengineering'
limit = 5
timeframe = 'all'
listing = 'top'
EVENT_HUB_CONNECTION_STR = "Endpoint=sb://tpiuolab1.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=1j4xz6Ea7PDfr5kBbxfjSsLPKN+TIu+uq+AEhGgH5oA="
EVENT_HUB_NAME = "lab1"

async def sendData(r):
    async with producer:
        event_data_batch = await producer.create_batch()

        for i in range (10):
         data = r["data"]["children"][i]["data"]
         data = json.dumps(data, indent = 4)
         event_data_batch.add(EventData(data))

        await producer.send_batch(event_data_batch) 
        while True:
         pass    
  
 
def get_reddit(subreddit,listing,limit,timeframe):
    try:
        base_url = f'https://www.reddit.com/r/{subreddit}/{listing}.json?limit={limit}&t={timeframe}'
        request = requests.get(base_url, headers = {'User-agent': 'yourbot'})
    except:
        print('An Error Occured')
    return request.json()
 

r = get_reddit(subreddit,listing,limit,timeframe)

producer = EventHubProducerClient.from_connection_string(
        conn_str=EVENT_HUB_CONNECTION_STR, eventhub_name=EVENT_HUB_NAME
    )
asyncio.run(sendData(r)) 