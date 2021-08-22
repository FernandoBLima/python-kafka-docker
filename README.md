# python-kafka-docker
The main objective in this project was to learn how to create an application that sends and receives a message from Kafka, using Docker and docker-compose tools.

## Stack

- aiokafka
- Docker
- FastAPI
- Kafka-python
- Python 3.8

## How to use

### Using Docker Compose 
You will need Docker installed to follow the next steps. To create and run the image use the following command:

```bash
> docker-compose up --build
```

The configuration will create a cluster with 3 containers:

- Consumer container
- Publisher container
- kafka container
- kafdrop container
- zookeeper container

The Publisher container will create a simple RESTful API application that sends data to Kafka. It will take a few seconds to come up, then will be accessible at `http://localhost:8000`.

The Consumer container is a script that aims to wait and receive messages from Kafka.

And the kafdrop container will provide acess to  web UI for viewing Kafka topics and browsing consumer groups that can be accessed at `http://localhost:19000`.


### API

- Send Message
  
Send message to Kafka, below is an example request:
```json
POST http://localhost:8000/producer
Accept: application/json
Content-Type: application/json
Body:
{
    "name": "value",
    "description": "value",
}
```


- Health check
  
Checks if the app is available.
```json
GET http://localhost:8000/
Accept: application/json
Content-Type: application/json
```

### Swagger

The swagger, an automatic interactive API documentation, will be accessible at `http://localhost:8000/docs`


## Project Structure
Below is a project structure created:
```cmd
.
├── README.md
├── docker-compose.yml
├── consumer
│   ├── Dockerfile
│   ├── app
│   │   ├── __init__.py
│   │   ├── __main__.py
│   │   └── enum.py
│   ├── app.py
│   └── requirements.txt
└── publisher
    ├── Dockerfile
    ├── app
    │   ├── __init__.py
    │   ├── core
    │   │   ├── __init__.py
    │   │   ├── gateways
    │   │   │   ├── __init__.py
    │   │   │   └── kafka.py
    │   │   └── models
    │   │       ├── __init__.py
    │   │       └── message.py
    │   ├── dependencies
    │   │   ├── __init__.py
    │   │   └── kafka.py
    │   ├── enum.py
    │   ├── main.py
    │   └── routers
    │       ├── __init__.py
    │       └── publisher.py
    └── requirements.txt
```

## Environment Variables
Listed below are the environment variables needed to run the application. They can be included in docker-compose or to run locally, it's necessary to create an `.env` file in the root of the Publisher and Consumer service folders.

- Publisher:
```bash
KAFKA_TOPIC_NAME=
KAFKA_SERVER=
KAFKA_PORT=
```

- Consumer:
```bash
KAFKA_TOPIC_NAME=
KAFKA_SERVER=
KAFKA_PORT=
```


## Help and Resources
You can read more about the tools documentation:

- [aiokafka](https://aiokafka.readthedocs.io/en/stable/ka)
- [Docker](https://docs.docker.com/get-started/overview/)
- [FastAPI](https://fastapi.tiangolo.com)
- [Kafdrop](https://github.com/obsidiandynamics/kafdrop)
- [Kafka](https://kafka.apache.org)
- [Kafka-python](https://kafka-python.readthedocs.io/en/master/)