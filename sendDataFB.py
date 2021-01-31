from firebase import firebase
from datetime import datetime
import time
import datetime
import RPi.GPIO as GPIO
import Adafruit_MCP3008

am = Adafruit_MCP3008.MCP3008(clk = 11, cs = 8, miso = 9, mosi = 10) 

WMD_SERIAL_NUMBER = '001' 

print("Program started!!!")

FBConn = firebase.FirebaseApplication('https://water-me-433c0-default-rtdb.firebaseio.com/',None)
print("Firebase connection established")

#reset
url = '/WMD/WMD-001/'
result = FBConn.get(url,None)
if(result != None):
    Entries = list(result.keys())
    for entry in Entries:
        FBConn.delete(url,entry)
print("Firebase data reset done")

#first entry
maxVal = 838  
soilMoisture = am.read_adc(0)
percentage = soilMoisture*100/maxVal
dateTime = datetime.datetime.now()
data_to_upload = {
    'Soil Moisture' : soilMoisture,
    'Moisture Percentage' : percentage,
    'Time Elapsed' : 0
}
result = FBConn.post(url, data_to_upload)
print(result)

while True:
    time.sleep(2)

    oldSoilMoisture = soilMoisture
    soilMoisture = am.read_adc(0)
    percentage = soilMoisture*100/maxVal 
    changeMoisture = soilMoisture - oldSoilMoisture 

    if(changeMoisture != 0):
        oldDateTime = dateTime
        dateTime = datetime.datetime.now()
        changeDateTime = dateTime - oldDateTime
        
        result = FBConn.get(url,None)
        lastEntry = list(result.keys())[0]
        FBConn.delete(url,lastEntry)

        print("Soil Moisture:",soilMoisture)
        print("Moisture Percentage:",percentage)
        print("Time Elapsed:",changeDateTime)

        data_to_upload = {
            'Soil Moisture' : soilMoisture,
            'Moisture Percentage' : percentage,
            'Time Elapsed' : changeDateTime
        }
    
        result = FBConn.post(url, data_to_upload)
        
        print(str(changeDateTime))
        print(result)


