import sys
import urllib2
import RPi.GPIO as GPIO
import Adafruit_DHT
# Write API Key ThingSpeak.com
miWriteAPIKey = "XXXXXXXXXXXXXXXX"
# Número GPIO de conexión out del sensor dht22 a RaspberryPi
raspiNumGPIO = "X"
def getSensorData():
   RH, T = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, raspiNumGPIO)
   return (str(RH), str(T))
def main():
   print 'Iniciando...'
   baseURL = 'https://api.thingspeak.com/update?api_key=%s' % miWriteAPIKey
   while True:
       try:
           RH, T = getSensorData()
           f = urllib2.urlopen(baseURL + "&field1=%s&field2=%s" % (RH, T))
           print f.read()
           f.close()
           sleep(5)
       except:
           print 'Terminado.'
           break
if __name__ == '__main__':
   main()
   
