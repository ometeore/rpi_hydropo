#import RPi.GPIO as GPIO 
import time
from random import randint
from classes.use_file import Use_file


############### SWITCH ON AND OFF Of Different motors light and EV

# def water_start():
#     GPIO.setmode(GPIO.BCM)
#     GPIO.setwarnings(False)
#     GPIO.setup(18,GPIO.OUT) 
#     GPIO.output(18,True)

# def water_stop():
#     GPIO.setmode(GPIO.BCM)
#     GPIO.setwarnings(False)
#     GPIO.setup(18,GPIO.OUT)
#     GPIO.output(18,False)

# def light_start():
#     GPIO.setmode(GPIO.BCM)
#     GPIO.setwarnings(False)
#     GPIO.setup(18,GPIO.OUT) 
#     GPIO.output(18,True)

# def light_stop():
#     GPIO.setmode(GPIO.BCM)
#     GPIO.setwarnings(False)
#     GPIO.setup(18,GPIO.OUT)
#     GPIO.output(18,False)


# def ph_start():
#     GPIO.setmode(GPIO.BCM)
#     GPIO.setwarnings(False)
#     GPIO.setup(23,GPIO.OUT) 
#     GPIO.output(23,True)

# def ph_stop():
#     GPIO.setmode(GPIO.BCM)
#     GPIO.setwarnings(False)
#     GPIO.setup(23,GPIO.OUT)
#     GPIO.output(23,False)


# def conduct_start():
#     GPIO.setmode(GPIO.BCM)
#     GPIO.setwarnings(False)
#     GPIO.setup(24,GPIO.OUT) 
#     GPIO.output(24,True)

# def conduct_stop():
#     GPIO.setmode(GPIO.BCM)
#     GPIO.setwarnings(False)
#     GPIO.setup(24,GPIO.OUT)
#     GPIO.output(24,False)


###################################### RECEPTION OF ANALOGIC ENTRANCE OF PH AND EC

######### For now the analogic captor are out to make the test i use randint close to the expected value

# So here we are using use file to get the expected value wich is not what we want to do
# as soon as the analog captor return a value. Get rid of that part

def ph_mesure():
    """function wich return true ph"""
    my_file = Use_file("schedule.txt")
    dict_schedule = my_file.file_to_dict()
    expected_ph = ((dict_schedule['ph'])*256)/14 + randint(-10, 10)

    return ph_transform(expected_ph)


def ec_mesure():
    """function that return true ec"""
    my_file = Use_file("schedule.txt")
    dict_schedule = my_file.file_to_dict()
    expected_ec = dict_schedule['ec'] + randint(-30, 30)

    return expected_ec



########################### THIS PART WILL NEED TO BE CALIBRATE

def ph_transform(analog_value):
    """ Transform the analogic version of ph (value from 0 -> 256) to the equivalent in ph 
        active calibration: val = 0 <-> ph = 0 // val = 256 <-> ph = 14
        q = 256 / 14""" 
    return (14*int(analog_value))/256

def ec_transform(analog_value):
    """read ph_transform and replace ph by ec
       active calibration: val = 0 <-> ec = 0 // val = 256 <-> ph = 5600
       q = """
    return (5600*int(analog_value))/256