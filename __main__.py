from classes.rpi import Rpi, nominal
import threading
import errno
from socket import error as socket_error
import time
#############"ICI deux threads un ecoute le serveur l'autre met la rpi en mode nominal"
### thread1: ecoute sur le channel ws et écris les modifs demandé sur schedule.txt
### thread2: nominal lance les moteurs et light aux horaires souhaités

user_keep_going = True

while user_keep_going:
    rpi = Rpi()
    #check if rpi is connected to server
    while not rpi.is_connect:
        try:
            rpi.ecoute()
        except socket_error as err:
            print("cant access to server due to error:" + err)
        nominal()
        time.sleep(6)
