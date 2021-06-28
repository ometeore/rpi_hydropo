import time
import websocket
import json
import pprint
import threading
from datetime import datetime
from classes.use_file import Use_file

from classes.demonstration import *


class Rpi:
    """la classe rpi"""

    def __init__(self):
        """init la raspberry avec la config GPIO des settings
        et les valeurs des schedule"""
        self.is_connect = False
        self.manual = False
        self.ph_motor = False
        self.ec_motor = False
        self.water_motor = False
        self.light_motor = False

    ##################### externaliser l'adresse serveur dans une variable dans settings

    def ecoute(self):
        """la rpi est en attente d'un message du serveur
        les fonctions qui regissent les messages sont dans
        websocket_func"""

        my_file = Use_file("settings.txt")
        dict_settings = my_file.file_to_dict()

        ws = MyWebSocketApp(
            self,
            dict_settings["url"],
            on_message=on_message,
            on_error=on_error,
            on_close=on_close,
        )
        ws.on_open = on_open
        ws.run_forever()


################### Websocket custom class and functions


class MyWebSocketApp(websocket.WebSocketApp):
    def __init__(self, rpi, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rpi = rpi


def on_open(ws):
    ws.rpi.is_connect = True
    blink_party()
    def run(*args):
        i = 0
        print("#############################\nWorking")
        while True:
            if not ws.rpi.is_connect:
                i = 0 
                led_green_stop()
                break
            i = i + 1
            led_green_start()
            nominal()
            message = {"i": i}
            if i == 16:
                json_message = json.dumps(send_status())
                ws.send(json_message)
                i = 0
            time.sleep(60)

        ws.close()
        led_green_stop()
        print("thread terminating...")

    x = threading.Thread(target=run, args=())
    x.start()


def on_message(ws, message):
    pp = pprint.PrettyPrinter(indent=4)
    dict_message = json.loads(message)

    if dict_message["message"]["message"]["manual"]:
        print("User start manual mode")
        ws.rpi.manual = True
        task = {}
        task["action"], task["type"] = "on", dict_message["message"]["message"]["tool"]
        manual_mode(task)
        time.sleep(300)
    else:
        print("Back in schedule mode")
        my_file = Use_file("schedule.txt")
        my_file.write_dico(dict_message["message"]["message"])


def on_error(ws, error):
    print(error)


def on_close(ws):
    ws.rpi.is_connect = False
    print("### closed ###")

def nominal():
    """Switch on or off sensors and motors if datetime is in schedule"""
    my_file = Use_file("schedule.txt")
    next_task = my_file.find_task()
    time_now = datetime.now()

    if not next_task:
        print("no task at: {}:{}".format(time_now.hour, time_now.minute))
    else:
        for task in next_task:
            get_task_done(task)


def send_status():
    """get ph and ec from hardware and prepare a message to send"""

    my_file = Use_file("settings.txt")
    dict_settings = my_file.file_to_dict()
    message_to_send = {}
    message_to_send["rpi_name"] = dict_settings["rpi_name"]
    message_to_send["ph"] = ph_mesure()
    message_to_send["ec"] = ec_mesure()
    print(message_to_send)
    return message_to_send

def manual_mode(task):
    turn_everything_off()
    get_task_done(task)

def get_task_done(task):
    if task['type'] == 'water':
        if task['action'] == 'on':
            led_blue_start()
            water_start()
        if task['action'] == 'off':
            led_blue_stop()
            water_stop()
    if task['type'] == 'light':
        if task['action'] == 'on':
            led_yellow_start()
            light_start()
        if task['action'] == 'off':
            light_stop()
            led_yellow_stop()

def turn_everything_off():
    water_stop()
    light_stop()
    conduct_stop()
    ph_stop()
