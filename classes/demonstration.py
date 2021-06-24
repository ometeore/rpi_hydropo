import time
from random import randint
from classes.use_file import Use_file



###################################### RECEPTION OF ANALOGIC ENTRANCE OF PH AND EC

#### This part is make for run a demonstration program without the need of a raspberry py or analogic sensors
#### it use a random value around the one wich is expected in the file: files.schedule.txt

######################################################################################
############################ HERE IS FOR ANALOGIC SENSORS ############################
######################################################################################

def ph_mesure():
    """function wich return true ph"""
    my_file = Use_file("schedule.txt")
    dict_schedule = my_file.file_to_dict()
    expected_ph = ((dict_schedule["ph"]) * 256) / 14 + randint(-10, 10)

    return ph_transform(expected_ph)


def ec_mesure():
    """function that return true ec"""
    my_file = Use_file("schedule.txt")
    dict_schedule = my_file.file_to_dict()
    expected_ec = dict_schedule["ec"] + randint(-30, 30)

    return expected_ec


def ph_transform(analog_value):
    """Transform the analogic version of ph (value from 0 -> 256) to the equivalent in ph
    active calibration: val = 0 <-> ph = 0 // val = 256 <-> ph = 14
    q = 256 / 14"""
    return (14 * int(analog_value)) / 256


def ec_transform(analog_value):
    """read ph_transform and replace ph by ec
    active calibration: val = 0 <-> ec = 0 // val = 256 <-> ph = 5600
    q ="""
    return (5600 * int(analog_value)) / 256

######################################################################################
############################### HERE IS FOR LED CONTROL ##############################
######################################################################################

def blink_party():
    pass

def led_green_start():
    pass

def led_green_stop():
    pass

def led_yellow_start():
    pass

def led_yellow_stop():
    pass

def led_white_start():
    pass

def led_white_stop():
    pass

def led_blue_start():
    pass

def led_blue_stop():
    pass

######################################################################################
############################## HERE IS FOR MOTOR CONTROL #############################
######################################################################################

def water_start():
    pass

def water_stop():
    pass

def light_start():
    pass

def light_stop():
    pass

def ph_start():
    pass

def ph_stop():
    pass

def conduct_start():
    pass

def conduct_stop():
    pass