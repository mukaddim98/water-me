from gpiozero import DigitalInputDevice
import time
 
d0_input = DigitalInputDevice(21)
 
while True:
    if(d0_input.value):
        print(str(d0_input.value))
        print('Moisture threshold reached!!!')
        time.sleep(2)
    else:
        print('You need to water your plant')
        time.sleep(2)
