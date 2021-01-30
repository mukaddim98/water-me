from firebase import firebase
from datetime import datetime
from gpiozero import DigitalInputDevice
import time
import datetime

WMD_SERIAL_NUMBER = '001' 

print("Program started!")

FBConn = firebase.FirebaseApplication('https://water-me-433c0-default-rtdb.firebaseio.com/',None)
d0_input = DigitalInputDevice(21)
        
#reset
url = '/WMD/WMD-001/'
result = FBConn.get(url,None)
if(result != None):
    Entries = list(result.keys())
    for entry in Entries:
        FBConn.delete(url,entry)

#first entry
soilMoisture = d0_input.value
dateTime = datetime.datetime.now()
data_to_upload = {
    'Soil Moisture' : soilMoisture,
    'Time' : 0
}
result = FBConn.post(url, data_to_upload)
print(result)

while True:
    time.sleep(2)

    oldSoilMoisture = soilMoisture
    soilMoisture = d0_input.value
    changeMoisture = soilMoisture - oldSoilMoisture 

    if(changeMoisture != 0):
        oldDateTime = dateTime
        dateTime = datetime.datetime.now()
        changeDateTime = dateTime - oldDateTime
        
        result = FBConn.get(url,None)
        lastEntry = list(result.keys())[0]
        FBConn.delete(url,lastEntry)

        if(soilMoisture):
            print('Moisture threshold reached!!!')
        else:
            print('You need to water your plant')

        data_to_upload = {
            'Soil Moisture' : soilMoisture,
            'Time' : changeDateTime
        }
    
        result = FBConn.post(url, data_to_upload)
        
        print(str(changeDateTime))
        print(result)


