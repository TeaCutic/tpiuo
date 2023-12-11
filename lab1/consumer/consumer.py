from azure.eventhub import EventHubConsumerClient

CONN_STR = "Endpoint=sb://tpiuolab1.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=1j4xz6Ea7PDfr5kBbxfjSsLPKN+TIu+uq+AEhGgH5oA="
EVENTHUB_NAME = "lab1"
CONSUMER_GROUP = "$Default"

client = EventHubConsumerClient.from_connection_string(CONN_STR, CONSUMER_GROUP, eventhub_name=EVENTHUB_NAME)


def on_event(partition_context, event):
    print(event.body_as_str(encoding='UTF-8'))
    partition_context.update_checkpoint(event)


with client:
    client.receive(on_event=on_event)
print("DONE!")
