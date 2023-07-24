print("MQTT with Adafruit IO")
print("Sensors and Actuators")

import time
import random
import serial.tools.list_ports
import sys
from Adafruit_IO import MQTTClient
import requests

AIO_USERNAME = "HTQ"
AIO_KEY = ""

global_equation = "x1 + x2 + x3"


def init_global_equation():
    headers = {}
    aio_url = "https://io.adafruit.com/api/v2/HTQ/feeds/equation"
    x = requests.get(url=aio_url, headers=headers, verify=False)
    data = x.json()



def connected(client):
    print("Server connected ...")
    client.subscribe("Button 1")
    client.subscribe("Button 2")
    client.subscribe("equation")


def subscribe(client, userdata, mid, granted_qos):
    print("Subscribeb!!!")


def disconnected(client):
    print("Disconnected from the server!!!")
    sys.exit(1)


def message(client, feed_id, payload):
    print("Received: " + payload)
    print("Testing commands")
    sendCommand(payload)


try:
    ser = serial.Serial(port="COM4", baudrate=115200)
except:
    print("Can not open the port")

def sendCommand(cmd):
    ser.write(cmd.encode())

mess = ""
def processData(data):
    print(data)
    data = data.replace("!", "")
    data = data.replace("#", "")
    splitData = data.split(":")
    print(splitData)
    if splitData[1] == "T":
        client.publish("sensor1", splitData[2])
    elif splitData[1] == "H":
        client.publish("sensor2", splitData[2])

def readSerial():
    bytesToRead = ser.inWaiting()
    if (bytesToRead > 0):
        global mess
        mess = mess + ser.read(bytesToRead).decode("UTF-8")
        while ("#" in mess) and ("!" in mess):
            start = mess.find("!")
            end = mess.find("#")
            processData(mess[start:end + 1])
            if (end == len(mess)):
                mess = ""
            else:
                mess = mess[end+1:]

def requestData(cmd):
    sendCommand(cmd)
    time.sleep(1)
    readSerial()


client = MQTTClient(AIO_USERNAME, AIO_KEY)

client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe

client.connect()
client.loop_background()
init_global_equation()

while True:
    requestData("0")
    time.sleep(2)
    requestData("1")
    time.sleep(2)


    pass