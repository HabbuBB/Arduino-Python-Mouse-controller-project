
# DIY Mouse controller using Arduino and Python

This is a project I did as a hobby for myself. This repository will include the instructions on how to create it yourself, and is a small, fun project for beginners.

The finished product lets you control your mouse with the joystick.

It's a fun project to show to your friends. Watching people struggle with video games using this controller is a great activity.



## What you need for this project

[Python](https://www.python.org/downloads/)

Python libraries
```bash
  py -m pip install mouse
  py -m pip install pyserial
  py -m pip install keyboard
```

Arduino Elego Uno R3

[Arduino program](https://www.arduino.cc/en/software)

Joystick module and four (4) Female-to-male Dupont wires

_I personally used [Elegoo Super Starter Kit for UNO](https://www.elegoo.com/products/elegoo-uno-project-super-starter-kit)_
## Wiring diagram

![Screenshot of Arduino board](https://github.com/HabbuBB/Arduino-Python-Mouse-controller-project/blob/master/img/DemoPicture.jpg)


Great for beginners!


## Step by step instructions

__1)__ Use the wiring diagram above to assemble your controller

__2)__ Clone this Github repository to your computer

__3)__ Paste the _mouse_arduino.ino_ file to your own Arduino project

__4)__ Plug in your Arduino and run the program. Open serial monitor to make sure it's working

![Screenshot of Arduino serial port input](https://github.com/HabbuBB/Arduino-Python-Mouse-controller-project/blob/master/img/serialportDemo.PNG)

_The serial port shows the input as following: 

X-coordinates:Y-coordinates:Mouse input

__5)__ Run the _mouse_arduino_fetcher.py_ file 

__6)__ Use the joystick, and control your mouse with it 

⚠️To forcestop the controller, press 0 on your keyboard⚠️

There you go, enjoy your controller!
## 🔗 Links


[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/aleksi-hannula-127007226/)

[__My github__](https://github.com/HabbuBB/)
