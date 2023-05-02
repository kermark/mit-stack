import paho.mqtt.client as mqtt
import random
import time

broker_address = "localhost"
broker_port = 1883
topic1 = "bmetk/esp1/demo1"
topic2 = "bmetk/esp2/demo2"
topic3 = "bmetk/esp2/demo3"
topic4 = "other/esp1/demo1"



client_id = f"python-mqtt-{random.randint(0, 1000)}"
client = mqtt.Client(client_id=client_id)
client.connect(broker_address, broker_port)

client.loop_start()

while True:
    random_int = random.randint(0, 100)
    client.publish(topic1, random_int)
    client.publish(topic2, random_int+100)
    client.publish(topic3, random_int+50)
    time.sleep(5)
