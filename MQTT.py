import time
import random
import sys
from Adafruit_IO import MQTTClient

AIO_FEED_ID = {"Button 1", "Button 2"}
AIO_USERNAME = "HTQ"
AIO_KEY = "aio_utVA6284dJjb7b1Tyx93RPWuiz3z"

def connected(client):
    print("Ket noi thanh cong ...")
    client.subscribe("Button 1")
    client.subscribe("Button 2")

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)

def message(client , feed_id , payload):
    print("Nhan du lieu: " + payload)

client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()

while True:
    time.sleep(5)
    client.publish("Sensor 1", random.randint(0, 100))
    client.publish("Sensor 2", random.randint(0, 100))
    client.publish("Sensor 3", random.randint(0, 100))
    pass
