.PHONY: install

install:
	./start.sh

.PHONY: start_zookeeper

start_zookeeper:
	zookeeper-server-start /etc/kafka/zookeeper.properties

.PHONY: start_kafka_server

start_kafka_server:
	kafka-server-start /etc/kafka/server.properties

.PHONY: check_kafka_topic

check_kafka_topic:
	kafka-console-consumer --bootstrap-server localhost:9092 --topic sf.crime.police.calls --from-beginning
