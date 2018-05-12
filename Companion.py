#! /usr/bin/env python

import serial
from serial import *
import time
from tkinter import *

ArduinoSerial = serial.Serial('/dev/ttyACM0', 9600, timeout=.1)

status1 = 0

# test now

def led_on():
    global status1
    ArduinoSerial.write(b'1')
    status1 = (ArduinoSerial.readline() ) # .decode('utf-8').strip())

def led_off():
    global status1
    ArduinoSerial.write(b'0')
    status1 = (ArduinoSerial.readline() ) # .decode('utf-8').strip())

def led_Exit():
    global status1
    ArduinoSerial.write(b'0')
    status1 = "Quit"
    quit()

root = Tk()                                         # GUI window
root.title("Arduino Push Buttons")
btn1 = Button(root, text="Led on", command=led_on)
btn2 = Button(root, text="Led off", command=led_off)
btn3 = Button(root, text="Exit", command=led_Exit)
msg1 = Label (root, textvariable = status1, relief=RAISED,width = 10)
btn1.pack()
btn2.pack()
btn3.pack()
msg1.pack()
root.mainloop()

