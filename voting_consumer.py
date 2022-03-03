#!/usr/bin/env python
"""Bare bones consumer with a listening loop"""

import time
import json
from confluent_kafka import Consumer

consumer_config = {'bootstrap.servers': 'localhost:9092', 'group.id': 'python_example_group_1'}
consumer = Consumer(consumer_config)

topic = 'votes'

key_value_counts = {}

consumer.subscribe([topic])

count = 0

try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            print("Waiting...")
        elif msg.error():
            print(f"ERROR: {msg.error()}")
        else:
            key = msg.key().decode('utf-8')
            val = msg.value().decode('utf-8')
            print(f"Consumed event: key={key}, value={val}")
            count += 1
            if key not in key_value_counts:
                key_value_counts[key] = {}

            if val not in key_value_counts[key]:
                key_value_counts[key][val] = 1
            else:
                key_value_counts[key][val] += 1

except KeyboardInterrupt:
    pass
finally:
    print("\n\nClosing out session")
    consumer.close()
    with open('vote_tallies.json', 'w') as vote_file:
        vote_file.write(json.dumps(key_value_counts, indent=2))
    print(f"This session consumed {count} total records")
    print("Goodbye.")