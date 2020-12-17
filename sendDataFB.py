from firebase import firebase
from datetime import datetime
import time

FBConn = firebase.FirebaseApplication('https://water-me-433c0-default-rtdb.firebaseio.com/',None)

while True:
    soilMoisture = 12;
    dateTime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    data_to_upload = {
        'Soil Moisture' : soilMoisture,
        'Time' : dateTime
    }
    
    url = '/MyTestData/'
    result = FBConn.post(url, data_to_upload)

    print(result)

    time.sleep(2)

    result = FBConn.get('/MyTestData/', None)
    lastEntry = list(result.keys())[0]
    FBConn.delete('/MyTestData/', lastEntry)
