import mouse
import time 
import serial
import keyboard

forceStop = True
mouse.FAILSAFE=False

mousehold = 0

try: 
   ArduinoSerial=serial.Serial('com3',9600)  #Specify the correct COM port, change if needed
   data=str(ArduinoSerial.readline().decode('ascii'))   #read the data
   time.sleep(1)                             #delay of 1 second

except:
   print("No data output found.") #Print out a message, if the program is not able to connect to your Arduino port
   forceStop = False

while forceStop:
   if keyboard.is_pressed('0'): #When user presses 0, the program forcestops.
       forceStop = False

   if (len(data) > 5):
     (y,x,z)=data.split(":")           # assigns to x,y and z (y and x flipped because of controller orientation)
     (x,y)=(int(x),int(y))  #convert x and y to int

     # If you want to switch your controller orientation, comment this
     if (y < 0):         
          y = abs(y)         
     else: 
          y = -abs(y)

     if (x < 0):  
          x = abs(x)      
     else:  
          x = -abs(x)

     (X,Y)=mouse.get_position()        # read the cursor's current position
     mouse.move(X+x,Y-y)           # move cursor to desired position relative from current position
     if '0' in z:                        # read the Status of SW (Mouse button)
          mouse.press(button='left')   # holds left button

     if '1' in z:
          mouse.release(button='left') # releases left button
   else: 
        print("Controller data output is too short")
