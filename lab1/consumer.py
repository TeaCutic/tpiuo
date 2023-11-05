import asyncio
from azure.eventhub.aio import EventHubConsumerClient

connection_str = "Endpoint=sb://tpiuolab1.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=1j4xz6Ea7PDfr5kBbxfjSsLPKN+TIu+uq+AEhGgH5oA="
consumer_group = "$default"
eventhub_name = "lab1"
client = EventHubConsumerClient.from_connection_string(connection_str, consumer_group, eventhub_name=eventhub_name)


async def on_event(partition_context, event):
    print(
        'Message data: {}'.format(
            event.body_as_str(encoding="UTF-8")
        )
    )
    await partition_context.update_checkpoint(event)

async def main():
    client = EventHubConsumerClient.from_connection_string(connection_str, consumer_group, eventhub_name=eventhub_name)
    async with client:
        await client.receive(on_event=on_event, starting_position="-1")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())


