import RPi.GPIO as GPIO 
import time

def water_start():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(18,GPIO.OUT) 
    GPIO.output(18,True)

def water_stop():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(18,GPIO.OUT)
    GPIO.output(18,False)

def light_start():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(18,GPIO.OUT) 
    GPIO.output(18,True)

def light_stop():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(18,GPIO.OUT)
    GPIO.output(18,False)


def ph_start():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(23,GPIO.OUT) 
    GPIO.output(23,True)

def ph_stop():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(23,GPIO.OUT)
    GPIO.output(23,False)


def conduct_start():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(24,GPIO.OUT) 
    GPIO.output(24,True)

def conduct_stop():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(24,GPIO.OUT)
    GPIO.output(24,False)
