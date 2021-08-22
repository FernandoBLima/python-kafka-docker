from app.core.gateways.kafka import Kafka


def get_kafka_instance():
    if Kafka.instance:
        return Kafka.instance
    return Kafka()
