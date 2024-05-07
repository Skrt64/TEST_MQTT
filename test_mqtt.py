import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
import time
import json

import random


port = 1883 # default port
Server_ip = "localhost"

Publish_Topic = "/test"
Subscribe_Topic = "/test_sub"


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    print("Connected.")
    client.subscribe(Subscribe_Topic)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
           

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.subscribe(Subscribe_Topic)
client.connect(Server_ip, port)
client.loop_start()

while True:
        
        data = {
        "R": random.randint(0,9),
        "G": random.randint(0,9),
        "B": random.randint(0,9)
        }
        data_out=json.dumps(data) # encode object to JSON
        publish.single(Publish_Topic ,data_out,hostname=Server_ip)

        print ("Publish.....")
        time.sleep(2)
