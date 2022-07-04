#!python3
import paho.mqtt.client as mqtt  #import the client1
import time

def on_connect(client, userdata, flags, rc):
    if rc==0:
        client.connected_flag=True #set flag
        print("connected OK")
    else:
        print("Bad connection Returned code=",rc)

def on_message(client, userdata, message):
    time.sleep(1)
    print("received message =",str(message.payload.decode("utf-8")))


mqtt.Client.connected_flag=False#create flag in class
broker="broker.mqttdashboard.com"
port=1883
client = mqtt.Client("clientId-lUfDDEJCUm")             #create new instance
#client.username_pw_set(username="Ubido",password="password")

client.on_connect=on_connect  #bind call back function
client.on_message=on_message
client.loop_start()
print("Connecting to broker ",broker)
try:
    client.connect(broker)      #connect to broker

    print("subscribing ")
    client.subscribe("testtopic/1")  # subscribe
    time.sleep(2)
    print("publishing ")
    client.publish("testtopic/1", "onn")  # publish
    time.sleep(4)

except Exception as e:
    print(e)

while not client.connected_flag: #wait in loop
    print("In wait loop")
    time.sleep(1)
print("in Main Loop")
client.loop_stop()    #Stop loop
print(client.subscribe("testtopic/1"))
client.disconnect() # disconnect


#client.publish("house/light", 1)