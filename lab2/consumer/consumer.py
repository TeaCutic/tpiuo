import asyncio
from azure.eventhub.aio import EventHubConsumerClient
from azure.storage.filedatalake import DataLakeServiceClient
import json
import datetime

connection_str ="Endpoint=sb://tpiuolab1.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=1j4xz6Ea7PDfr5kBbxfjSsLPKN+TIu+uq+AEhGgH5oA="
consumer_group = "$default"
eventhub_name = "lab1"
client = EventHubConsumerClient.from_connection_string(connection_str, consumer_group, eventhub_name=eventhub_name)

container_name="sl-container"
connection_string_sl = "DefaultEndpointsProtocol=https;AccountName=tpioustoragelake;AccountKey=83qMNtwGo0uaZ0NYoudmlna7DziWb5nJp4w0f9DYzV00XiI3MCLHTfP85ZAboeSzNQUe9ay6kFuF+AStwISi3w==;EndpointSuffix=core.windows.net"
service_client = DataLakeServiceClient.from_connection_string(connection_string_sl)

async def on_event(partition_context, event):
    print("Got data")
    data = json.loads(event.body_as_str(encoding="UTF-8"))
    date = data["created_utc"]
    directory_name = datetime.datetime.utcfromtimestamp(date).strftime('%Y/%m/%d/%H/%M')

    file_system_client = service_client.get_file_system_client(file_system=container_name)
    dir_client = file_system_client.get_directory_client(str(directory_name))
    dir_client.create_directory()
    file_name = str(data["id"])
    file_client = dir_client.create_file(file_name + ".txt")
    data = json.dumps(data)
    file_client.append_data(data, 0, len(data))
    file_client.flush_data(len(data))

    await partition_context.update_checkpoint(event)

async def main():
    async with client:
        await client.receive(on_event=on_event)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main()) 


