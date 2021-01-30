import RPi.GPIO as GPIO
from time import sleep
import Adafruit_MCP3008

am = Adafruit_MCP3008.MCP3008(clk = 11, cs = 8, miso = 9, mosi = 10)

while True:
  maxVal = 838  
  moisture_value = am.read_adc(0) # Get the analog reading from the soil moist sensor
  per = moisture_value * 100 / maxVal  # Converting the moisture value to percentage
  print("Moisture Value: "+str(moisture_value));
  print("Recorded moisture value is %s percentage" % per)
  if per >= 70:
    print("Stop! I will vomit.")
  elif moisture_value < 70 and moisture_value >= 30:
      print("Hey, I'm full :D")
  elif moisture_value < 30 :
    print("Yo, I'm thirsty!")
  sleep(1.5)
