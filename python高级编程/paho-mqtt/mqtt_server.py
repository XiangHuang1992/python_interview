import paho.mqtt.client as mqtt
import time

HOST = '127.0.0.1'
PORT = 1883


def client_loop():
    client_id = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    client = mqtt.Client(client_id)
    client.username_pw_set('admin', password='123456')
    client.on_connect = on_connect
    client.on_message = on_message
    try:
        client.connect(HOST, PORT, 60)
        client.loop_forever()
    except KeyboardInterrupt:
        client.disconnect()


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("test")


def on_message(client, userdata, msg):
    print(msg.topic+" " + msg.payload.decode("utf-8"))


if __name__ == "__main__":
    client_loop()
