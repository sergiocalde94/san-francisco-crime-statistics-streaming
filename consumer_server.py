from kafka import KafkaConsumer


TOPIC_NAME = 'sf.crime.police.calls'
BOOTSTRAP_SERVER='localhost:9092'

try:
    consumer = KafkaConsumer(bootstrap_servers=BOOTSTRAP_SERVER,
                             auto_offset_reset='earliest',
                             consumer_timeout_ms=1_000)
except Exception as e:
    print('Fail when creating KafkaConsumer.')
    raise e

try:
    consumer.subscribe([TOPIC_NAME])
except Exception as e:
    print(f'Fail when subscribing to {TOPIC_NAME} topic.')
    raise e

for message in consumer:
    print(message.value)
