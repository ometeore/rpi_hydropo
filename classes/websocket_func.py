from classes.use_file import Use_file
# from classes.moteur_ev import *
# from classes.led import *
import json
import pprint
import time
import threading

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

def on_open(ws):
	def run(*args):
		print("#############################\n Working")
		while True:
			nominal()
			time.sleep(60)
			
		ws.close()
		print("thread terminating...")
	x = threading.Thread(target=run, args=())
	x.start()



################### MANAGER

def nominal():
	""" Switch on or off sensors and motors if datetime is in schedule """
	my_file = Use_file("schedule.txt")
	next_task = my_file.find_task()
	print(next_task)
	schedule = my_file.file_to_dict()

def get_task_done(task):
	pass
