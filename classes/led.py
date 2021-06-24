import RPi.GPIO as GPIO
import time


#####
# controle des leds
# 26 vert
# 19 jaune
# 13 blanc
# 6 bleu


def blink_party():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(6, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(19, GPIO.OUT)
    GPIO.setup(26, GPIO.OUT)
    nbr_de_boucle = 3
    while nbr_de_boucle > 0:
        GPIO.output(6, True)
        time.sleep(0.2)
        GPIO.output(13, True)
        GPIO.output(6, False)
        time.sleep(0.2)
        GPIO.output(19, True)
        GPIO.output(13, False)
        time.sleep(0.2)
        GPIO.output(26, True)
        GPIO.output(19, False)
        time.sleep(0.2)
        GPIO.output(26, False)
        nbr_de_boucle = nbr_de_boucle - 1
    GPIO.output(26, True)
    GPIO.output(19, True)
    GPIO.output(13, True)
    GPIO.output(6, True)
    time.sleep(2)
    GPIO.output(6, False)
    GPIO.output(13, False)
    GPIO.output(19, False)
    GPIO.output(26, False)


def led_green_start():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(26, GPIO.OUT)
    GPIO.output(26, True)


def led_green_stop():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(26, GPIO.OUT)
    GPIO.output(26, False)


def led_yellow_start():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(19, GPIO.OUT)
    GPIO.output(19, True)


def led_yellow_stop():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(19, GPIO.OUT)
    GPIO.output(19, False)


def led_white_start():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(13, GPIO.OUT)
    GPIO.output(13, True)


def led_white_stop():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(13, GPIO.OUT)
    GPIO.output(13, False)


def led_blue_start():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(6, GPIO.OUT)
    GPIO.output(6, True)


def led_blue_stop():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(6, GPIO.OUT)
    GPIO.output(6, False)
