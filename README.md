# kafka-python-docker-example
Experiment project with Docker, Docker Compose, Python and Kafka. The pipeline is:

(HTTP POST) => `Endpoint` => `Kafka` (Raw data topic) => `Parser` => `Kafka` (Parsed data topic) => `Persister`

Currently we are just passing the same message from the HTTP POST request all the way to the end of the pipeline.

## Requirements
- Docker (and Docker Compose)

## Setup & Run
```
$ git clone git@github.com:pjlampil/kafka-python-docker-example.git
$ cd kafka-python-docker-example
$ docker-compose up
```

### Run migrations
```
$ docker-compose exec api ./manage.py migrate
```

## Usage
Following command will send a message (with somewhat random value) every two seconds until quit. It sends a HTTP POST to the endpoint to simulate the real world scenario.
```
$ docker-compose exec persister ./manage.py send_messages 2
```

## API
API can be found by default from http://localhost:8001/observations

## Example Frontend
An example frontend that uses API and visualizes the data can be found by default from http://localhost:8002/
