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

## Usage

You can send messages to the `endpoint` by sending a HTTP POST with a parameter `value` set. Example:

```
curl --request POST \
  --url http://localhost:8000/ \
  --header 'content-type: application/x-www-form-urlencoded' \
  --data 'value=this is a test message'
```

## TODO

- Currently `Persister` is just a python script. We should introduce the Django framework here to make it more real world example.
