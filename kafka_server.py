import producer_server


TOPIC_NAME = 'sf.crime.police.calls'
BOOTSTRAP_SERVER='localhost:9092'
CLIENT_ID = 'sf_crime_consumer'
PATH_INPUT_FILE = 'police-department-calls-for-service.json'

def run_kafka_server():
    # TODO get the json file path
    input_file = PATH_INPUT_FILE

    # TODO fill in blanks
    producer = producer_server.ProducerServer(
        input_file=input_file,
        topic=TOPIC_NAME,
        bootstrap_servers=BOOTSTRAP_SERVER,
        client_id=CLIENT_ID
    )

    return producer


def feed():
    producer = run_kafka_server()
    producer.generate_data()


if __name__ == "__main__":
    feed()
