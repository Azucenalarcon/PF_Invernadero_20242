import time
import adafruit_dht
import board
from RPLCD.i2c import CharLCD

lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1, cols=16, rows=2, dotsize=8)
lcd.clear()


dht_device = adafruit_dht.DHT11(board.D4)

def funcion():
    while True:
        try:
            tempe = dht_device.temperature
            humi = dht_device.humidity
            print("temp:{:.1f} C  humidity: {}%" .format(tempe, humi))
        except RuntimeError as err:
            #print(err.args[0])
            tempe=0
            humi=0
            #print("ho1: " +str(dht_device.temperature))
            #print("ho2: " +str(dht_device.humidity))
        time.sleep(2.0)
        return tempe, humi

while True:
    #lcd.clear()
    datos = funcion()
    humedad = datos[1]
    temperatura = datos[0]
    if (humedad!=0 and temperatura!=0):
        lcd.clear()
        print("temperatura: " +str(temperatura) + "humedad: " +str(humedad))
        lcd.write_string('Temperatura: ' +str(temperatura))
        lcd.cursor_pos = (1,0)
        lcd.write_string('Humedad: ' +str(humedad))


