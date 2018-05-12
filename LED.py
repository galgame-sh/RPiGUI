from tkinter import *
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

#hardware
blu = LED(14)
red = LED(15)
gre = LED(17)
#GUI DEFINITION

win = Tk()
win.title("LED")
var = IntVar()
#EVENT FUNCTIONS


def function():
    selection = var.get()
    if selection ==1:        
        red.off()
        blu.on()
        gre.off()
    elif selection ==2:        
        blu.off()
        red.on()
        gre.off()
    elif selection==3:          
        blu.off()
        red.off()
        gre.on()
    elif selection==4:        
        blu.off()
        red.off()
        gre.off()        
    else:
        selection==0


#WIDGET
yelButton = Radiobutton(win, text = 'Blue On',variable = var,value=1,command=function).grid(row=0,sticky=W)
redButton = Radiobutton(win, text = 'Red On',variable = var,value=2,command=function).grid(row=1,sticky=W)
GreenButton = Radiobutton(win, text = 'Green On',variable = var,value=3,command=function).grid(row=2,sticky=W)
GreenButton = Radiobutton(win, text = 'Close',variable = var,value=4,command=function).grid(row=3,sticky=W)
