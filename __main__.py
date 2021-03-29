from classes.rpi import Rpi
import threading

#############"ICI deux threads un ecoute le serveur l'autre met la rpi en mode nominal"
### thread1: ecoute sur le channel ws et écris les modifs demandé sur schedule.txt
### thread2: nominal lance les moteurs et light aux horaires souhaités


keep_going = True


while keep_going:
    rpi = Rpi()
    #rpi.nominal()
    rpi.ecoute()
    keep_going = False