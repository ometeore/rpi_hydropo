import time
import websocket
import json
import pprint
import threading
from datetime import datetime
from classes.use_file import Use_file 
# import only in production check down this file to un comment more in production
#import classes.hardware 


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


    ##################### externaliser l'adresse serveur dans une variable dans settings

    def ecoute(self):
        """ la rpi est en attente d'un message du serveur
        les fonctions qui regissent les messages sont dans
        websocket_func"""

        my_file = Use_file("settings.txt")
        dict_settings = my_file.file_to_dict()

        ws = MyWebSocketApp(
                            self,
                            dict_settings['url'],
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
            nominal()
            time.sleep(60)

        ws.close()
        print("thread terminating...")
    x = threading.Thread(target=run, args=())
    x.start()

def on_message(ws, message):
    pp = pprint.PrettyPrinter(indent=4)
    dict_message = json.loads(message)
    
    if dict_message['message']['message']['manual']:
        print("######## MANUAL MODE ########")
        ws.rpi.manual = True
        task = {}
        task['action'], task['type'] = 'on', dict_message['message']['message']['tool']
        manual_mode(task)
        time.sleep(300)
    else:
        print("######## SCHEDULE MODE ########")
        my_file = Use_file("schedule.txt")
        my_file.write_dico(dict_message['message']['message'])


def on_error(ws, error):
    print(error)

def on_close(ws):
    print(datetime.now())
    print("### closed ###")


def nominal():
    """ Switch on or off sensors and motors if datetime is in schedule """
    my_file = Use_file("schedule.txt")
    next_task = my_file.find_task()
    time_now = datetime.now()

    if not next_task:
        print("no task at: {}:{}".format(time_now.hour, time_now.minute))
    else:
        for task in next_task:
            print(task)
            get_task_done(task)

def turn_everything_off():
    pass




def manual_mode(task):
    turn_everything_off()
    get_task_done(task)

def get_task_done(task):
    pass

    ############# UNCOMMENT THIS IN PRODUCTION (and the import)

# def get_task_done(task):
#     if task['type'] == 'water':
#         if task['action'] == 'on':
#             water_start()
#         if task['action'] == 'off':
#             water_stop()
#     if task['type'] == 'light':
#         if task['action'] == 'on':
#             light_start()
#         if task['action'] == 'off':
#             light_stop()

# def turn_everything_off():
#     water_stop()
#     light_stop()
#     conduct_stop()
#     ph_stop()