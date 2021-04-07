import time
import websocket
import json
import pprint
import threading
from datetime import datetime
from classes.use_file import Use_file



class Rpi:
    """ la classe rpi """

    def __init__(self):
        """ init la raspberry avec la config GPIO des settings
         et les valeurs des schedule"""
        self.manual = False
        self.ph = False
        self.ec = False
        self.water = False
        self.light = False

    def ecoute(self):
        """ la rpi est en attente d'un message du serveur
        les fonctions qui regissent les messages sont dans
        websocket_func"""
        ws = MyWebSocketApp(
                            self,
                            "ws://127.0.0.1:8000/ws/",
                            on_message = on_message,
                            on_error = on_error,
                            on_close = on_close
                            )
        ws.on_open = on_open
        ws.run_forever()


################### Websocket custom class and functions

class MyWebSocketApp(websocket.WebSocketApp):
    def __init__(self, rpi, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rpi = rpi


def on_open(ws):
    def run(*args):
        print("#############################\nWorking")
        while True:
            nominal(ws.rpi)
            time.sleep(60)

        ws.close()
        print("thread terminating...")
    x = threading.Thread(target=run, args=())
    x.start()

def on_message(ws, message):
    pp = pprint.PrettyPrinter(indent=4)
    dict_message = json.loads(message)
    pp.pprint(dict_message['message']['message'])
    
    if dict_message['message']['message']['manual']:
        print("On est dans le mode manuel")

    else:
        print("A recu une demande de modification du scheduleur")
        my_file = Use_file("schedule.txt")
        my_file.write_dico(str(dict_message['message']['message']))


def on_error(ws, error):
    print(error)

def on_close(ws):
    print(datetime.now())
    print("### closed ###")


def nominal(rpi):
    """ Switch on or off sensors and motors if datetime is in schedule """
    my_file = Use_file("schedule.txt")
    next_task = my_file.find_task()
    time_now = datetime.now()

    if not next_task:
        print("no task at: {}:{}".format(time_now.hour, time_now.minute))
    else:
        for task in next_task:
            get_task_done(task)


def get_task_done(task):
    pass