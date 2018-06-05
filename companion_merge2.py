import serial
from serial import *
import time
from tkinter import *

ArduinoSerial = serial.Serial('COM11', 9600, timeout=.1)

status1 = 0

# test now

def Forward():
    global status1
    ArduinoSerial.write(b'0')
    status1 = (ArduinoSerial.readline() ) # .decode('utf-8').strip())
    print(1)

def Backward():
    global status1
    ArduinoSerial.write(b'1')
    status1 = (ArduinoSerial.readline() ) # .decode('utf-8').strip())
    print (0)

def Right():
    global status1
    ArduinoSerial.write(b'2')
    status1 = (ArduinoSerial.readline() ) # .decode('utf-8').strip())

def Left():
    global status1
    ArduinoSerial.write(b'3')
    status1 = (ArduinoSerial.readline() ) # .decode('utf-8').strip())

def GiveFood():
    global status1
    ArduinoSerial.write(b'4')
    status1 = (ArduinoSerial.readline() )

def CloseFood():
    global status1
    ArduinoSerial.write(b'5')
    status1 = (ArduinoSerial.readline() )    
    

def led_Exit():
    global status1
    ArduinoSerial.write(b'7')
    status1 = "Quit"
    quit()


root = Tk()                                         # GUI window
root.title("Arduino Push Buttons")
btn_frd = Button(root, text="Forward", command=lambda:Forward())
btn_bck = Button(root, text="Backward", command=lambda:Backward())
btn_lft = Button(root, text="Left", command=lambda:Left())
btn_rth = Button(root, text="Right", command=lambda:Right())
btn_gf = Button(root, text="Give Food", command=lambda:GiveFood())
btn_cf = Button(root, text="Close Food", command=lambda:CloseFood())
btn_exit = Button(root, text="Exit", command=lambda:led_Exit())

msg1 = Label (root, textvariable = status1, relief=RAISED,width = 10)
btn_frd.pack()
btn_bck.pack()
btn_rth.pack()
btn_lft.pack()
btn_gf.pack()
btn_cf.pack()
btn_exit.pack()
msg1.pack()
root.mainloop()
