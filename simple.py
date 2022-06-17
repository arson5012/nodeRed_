import network,time
from simple import MQTTClient 
from machine import I2C,Pin,Timer

step1 = 0

def WIFI_Connect():
    wlan = network.WLAN(network.STA_IF) 
    wlan.active(True)                  
    start_time=time.time()              

    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('WiFi ID', 'WiFi PW') 
        
    if wlan.isconnected():
        print('network information:', wlan.ifconfig())
        return True    

def MQTT_Send(tim):
    global step1
    client.publish(TOPIC, 'Hello jetson'+str(step1))
    step1 = step1 +1
    print(step1)

if WIFI_Connect():
    SERVER = 'IP'   
    PORT = 1883
    CLIENT_ID = '' # clinet id 이름
    TOPIC = '' # TOPIC 이름
    client = MQTTClient(CLIENT_ID, SERVER, PORT)
    client.connect()

   
    tim = Timer(-1)
    tim.init(period=1000, mode=Timer.PERIODIC,callback=MQTT_Send)


