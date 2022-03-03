# Kafka Voting System Concept

This is an exercise in understanding the very fundamentals of Kafka using a voting system as a use-case.
This is in no way scientific, it's simply an exercise to show how Kafka works as an event-streaming platform
in a way that is relatable to the wider world.

## Requirements
In order to run this demo, you will need the following installed on your system.

- Docker CLI
- Python3
- Pipenv

## Setup
### Pipenv
Once you have cloned this repo to a local directory on your system, you should make sure that the pipenv is created 
correctly, and log into the shell. You can do so by simply running:
```text
$ pipenv install
```
Then entering the shell by running:
```text
$ pipenv shell
```
### Docker
Once you are in the virtual environment, run the following command to bring up the docker images:

```text
$ docker compose up -d
$ docker compose exec broker kafka-topics --create --topic votes --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1
```
Once you have run these commands, you should see the output below:
```text
Created topic votes.
```

With that out of the way, the topic has been created and the consumer should be ready to subscribe and listen 
for new events.

## Running the Consumer
The Consumer script in this repository is very bare-bones, and therefore is very simple to run. From within the pipenv 
shell, you can start up the consumer by running:

```text
./voting_consumer.py
```

This will begin the event loop within the script which will constantly print "Waiting..." until it ingests data from the 
topic. To exit, you can use a standard keyboard interrupt. This will finalize all the data and save it to a local json
file, and give a report of how many records were ingested.

NOTE: The json file overwritten every time this is run, and does not update from run to run.

## Running the Producer
In another terminal from within the pipenv, startup the voting producer script by running:
```text
./voting_producer.py
```

Once you do this, you will begin to see output of the votes being cast in the terminal.