import mouse
import time 
import serial
import keyboard
import sys


def main():
     forceStop = True
     mouse.FAILSAFE=False

     try: 
          ArduinoSerial=serial.Serial('com3',9600, timeout=.1)  #Specify the correct COM port, change if needed
          data=str(ArduinoSerial.readline().decode('ascii'))   #read the data
          time.sleep(1)                             #delay of 1 second

     except:
          print("No data output found.") #Print out a message, if the program is not able to connect to your Arduino port
          forceStop = False
          sys.exit()

     while forceStop:
          data=str(ArduinoSerial.readline().decode('ascii'))   #read the data
          if keyboard.is_pressed('0'): #When user presses 0, the program forcestops.
               forceStop = False
               sys.exit()

          if (len(data) > 4):
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

if __name__ == "__main__":
     main()
