import requests
import asyncio
import json
import time

from azure.eventhub import EventData
from azure.eventhub.aio import EventHubProducerClient
 
subreddit = 'dataengineering'
limit = 10
timeframe = 'all'
listing = 'top'
EVENT_HUB_CONNECTION_STR = "Endpoint=sb://tpiuolab1.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=1j4xz6Ea7PDfr5kBbxfjSsLPKN+TIu+uq+AEhGgH5oA="
EVENT_HUB_NAME = "lab1"

async def sendData(r):
     async with producer:
        event_data_batch = await producer.create_batch()

        for i in range (limit):
            data = r["data"]["children"][i]["data"]
            data = json.dumps(data, indent = 4)
            event_data_batch.add(EventData(data)) 

        await producer.send_batch(event_data_batch)    
        print("Data sent")  
  
 
def get_reddit(subreddit,listing,limit,timeframe,after_flag):
    try:
        base_url = f'https://www.reddit.com/r/{subreddit}/{listing}.json?limit={limit}&t={timeframe}&after={after_flag}'
        request = requests.get(base_url, headers = {'User-agent': 'yourbot'})
    except:
        print('An Error Occured')
    return request.json()
 

producer = EventHubProducerClient.from_connection_string(
        conn_str=EVENT_HUB_CONNECTION_STR, eventhub_name=EVENT_HUB_NAME
    )

after = 1
after_flag=None

while after == 1:
   r = get_reddit(subreddit,listing,limit,timeframe,after_flag)
   asyncio.run(sendData(r))
   after_flag = r['data']['after']
   if after_flag == None:
      after = 0
   else:
      time.sleep(10)
    
while 1==1:
   pass

