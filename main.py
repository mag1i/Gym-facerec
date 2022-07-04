#!python3
import paho.mqtt.client as mqtt  #import the client1
import time
import pymysql

def on_connect(client, userdata, flags, rc):
    if rc==0:
        client.connected_flag=True #set flag
        print("connected OK")
    else:
        print("Bad connection Returned code=",rc)

def on_message(client, userdata, message):
    time.sleep(1)


    con = pymysql.connect(host="localhost", user="root", password="1234", database="Gym")
    cur = con.cursor()
    cur.execute("SELECT  MAX(userid) from user")
    g = cur.fetchone()
    cur.execute( "update user set phone=%s WHERE userid=%s",(str(message.payload.decode("utf-8")), g))

    print("received message =",str(message.payload.decode("utf-8")))
bl =True
k=0
while (bl==True):
        mqtt.Client.connected_flag=False#create flag in class
        broker="broker.hivemq.com"
        port=1883

        client = mqtt.Client("clientId-lUfDDEJCUm")             #create new instance
        #client.username_pw_set(username="Ubido",password="password")

        client.on_connect=on_connect  #bind call back function
        client.on_message=on_message
        client.loop_start()
        print("Connecting to broker ",broker)
        try:
            client.connect(broker)      #connect to broker


        except Exception as e:
            print(e)

        while not client.connected_flag: #wait in loop
            print("In wait loop")
            time.sleep(1)
        print("in Main Loop")

        print("subscribing ")
        client.subscribe("Room/Lamp")  # subscribe
        time.sleep(2)
        #print("publishing ")

        #client.publish("Room/Lamp", "1")  # publish

        time.sleep(4)
        client.loop_stop()    #Stop loop
        print("here",client.subscribe("Room/Lamp"))


        client.disconnect() # disconnect


        #client.publish("house/light", 1)