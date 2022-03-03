#!/usr/bin/env python
"""Bare bones producer in the form of a voting simulation"""

import random
import time
from confluent_kafka import Producer

if __name__ == '__main__':
    # setup the configuration to be provided to the Producer() object
    conf = {'bootstrap.servers': 'localhost:9092'}

    topic = 'votes'

    # instantiate Producer object with config
    producer = Producer(conf)


    def delivery_callback(err, msg):
        """callback function to be called when the message is successfully published"""
        if err:
            print(f"ERROR: MESSAGE FAILED: {err}")
        else:
            print(f"Cast vote from state: {msg.key().decode('utf-8')}, candidate: {msg.value().decode('utf-8')}")

    # Supply lists of state codes and candidates for producer to randomly select from.
    states = ['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA',
              'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME',
              'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM',
              'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX',
              'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY']
    candidates = ["Dwayne 'The Rock' Johnson", "Matthew McConaughey", "Oprah Winfrey", "Kanye West"]

    # Start loop to produce randomized records.
    try:
        while True:
            key = random.choice(states)
            val = random.choice(candidates)
            producer.produce(topic, val, key, callback=delivery_callback)
            time.sleep(random.randint(0, 1))
            producer.poll(10000)
            producer.flush()
    except KeyboardInterrupt:
        pass
    finally:
        print("Exiting")
