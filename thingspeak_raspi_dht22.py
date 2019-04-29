import sys
import RPi.GPIO as GPIO
import Adafruit_DHT
import urllib2
miAPIWrite = "XXXXXXXXXXXXXXXX"
raspiGPIO = "X"
def getSensorData():
   RH, T = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, raspiGPIO)
   return (str(RH), str(T))
def main():
   print 'starting...'
   baseURL = 'https://api.thingspeak.com/update?api_key=%s' % miAPIWrite
   while True:
       try:
           RH, T = getSensorData()
           f = urllib2.urlopen(baseURL +
                               "&field1=%s&field2=%s" % (RH, T))
           print f.read()
           f.close()
           sleep(5)
       except:
           print 'exiting.'
           break
if __name__ == '__main__':
   main()
