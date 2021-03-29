from datetime import datetime
from classes.websocket_func import on_message, on_error, on_close, on_open
from classes.use_file import Use_file
import time
import websocket


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


    def status(self):
        """ return l'état de la rpi"""
        status = {
            'manual' : self.manual,
            'ph': self.ph,
            'ec': self.ec,
            'water':self.water,
            'lights': self.light
        }
        return status

    def ecoute(self):
        """ la rpi est en attente d'un message du serveur elle e"""
        ws = websocket.WebSocketApp("ws://127.0.0.1:8000/ws/",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
        ws.on_open = on_open
        ws.run_forever()