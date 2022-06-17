import time
from lsm6dsox import LSM6DSOX
import network,time
from simple import MQTTClient 
from machine import I2C,Pin,Timer
from machine import Pin, I2C

lsm = LSM6DSOX(I2C(0, scl=Pin(13), sda=Pin(12)))
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
    while (True):
        accel_x, accel_y, accel_z = lsm.read_accel()
        gyro_x, gyro_y, gyro_z = lsm.read_gyro()
        #자이로x는 10보다 크면 움직이는 상태
        #가속도x는 -0.1보다 크면 정지 상태
        #뛰면 z축이 많이 변동됨
        
        accx=round(accel_x,1)
        acc_x=accx / 16384.0
        accy=round(accel_y,1)
        acc_y=accy / 16384.0
        accz=round(accel_z,1)
        acc_z=accz / 16384.0
        
        gyrox=round(gyro_x,1)
        gyroy=round(gyro_y,1)
        gyroz=round(gyro_z,1)
        
        """
        cntx = list([acc_x])
        cnty = list([acc_y])
        cntz = list([acc_z])
        avgx = sum(cntx,0.0)/len(cntx)
        avgy = sum(cnty,0.0)/len(cnty)
        avgz = sum(cntz,0.0)/len(cntz)
        """
        cntx = list([gyrox])
        cnty = list([gyroy])
        cntz = list([gyroz])
        avgx = sum(cntx,0.0)/len(cntx)
        avgy = sum(cnty,0.0)/len(cnty)
        avgz = sum(cntz,0.0)/len(cntz)
        
        avgchart = sum((avgx,avgy,avgz),0.0)/len((avgx,avgy,avgz))
        
        client.publish('chart/x',"{0}".format(avgx))
        client.publish('chart/y',"{0}".format(avgy))
        client.publish('chart/z',"{0}".format(avgz))
        
        if (-0.1 >= avgx or 0.1 <= avgx) or (-0.1 >= avgy or 0.1 <= avgy) or (-0.1 >= avgz or 0.1 <= avgz):
            step1 = 0
        if (step1 == 1):
            continue
        if (-10 < avgx < 10) and (-10 < avgy < 10) and (-10 < avgz < 10): #감도 조정 필요
            print("Stop")  # 정지시
            step1 =1
            client.publish(TOPIC,'Stop')
            
        else:
            print("Move")
            client.publish(TOPIC,'Move')
            
        
        
        time.sleep(0.5)
        #client.publish('stopmqtt',client.disconnect())
        
            
        """
        if (-avgx < gyrox > avgx) and (-avgy < gyroy > avgy) and (-1.0 < avgz > 1.0):
            print("MOVE")
        else:
            print("Stop")
        
        
        if acc_y == 0:
            print("정지")
        
            
        print(avgx,avgy,avgz)#자이로x는 10보다 크면 움직이는 상태
                             #가속도x는 -0.1보다 크면 정지 상태
                             #뛰면 z축이 많이 변동됨
        """
        
        

if WIFI_Connect():
    #client.publish(TOPIC,"{0}".format(accx))
    SERVER = 'IP'
    PORT = 1883
    CLIENT_ID = '' # clinet id 이름
    TOPIC = 'gyro' # TOPIC 이름
    client = MQTTClient(CLIENT_ID, SERVER, PORT)
    client.connect()

   
    tim = Timer(-1)
    tim.init(period=1000, mode=Timer.PERIODIC,callback=MQTT_Send)





