import time
import adafruit_dht
import board

dht_device = adafruit_dht.DHT11(board.D4)

def funcion():
    while True:
        try:
            tempe = dht_device.temperature
            humi = dht_device.humidity
            print("temp:{:.1f} C  humidity: {}%" .format(tempe, humi))
        except RuntimeError as err:
            print(err.args[0])
            tempe=0
            humi=0
            print("ho1: " +str(dht_device.temperature))
            print("ho2: " +str(dht_device.humidity))
        time.sleep(2.0)
        return tempe, humi

while True:
    print("hola: " + str(funcion()))

