import os.path
import ast
import json
from datetime import datetime, date, timedelta
from pathlib import Path
#import pathlib

class Use_file:
    """ la classe pour lire et écrire dans les settings  """

    def __init__(self, name):
        self.path = Path('./files/' + name)

    ##### revoir ast literal pourri le code
    def file_to_dict(self):
        my_file = open(self.path, 'r')
        dico = ast.literal_eval(my_file.read())
        my_file.close()
        return dico

    def write_dico(self, dico):
        my_file = open(self.path, 'w')
        my_file.write(dico)
        my_file.close()

    def find_task(self):
        """ va recuperer les prochains horaire dans le fichier retourne l'heure 
        la tache et l'action (on/off)"""
        my_file = self.file_to_dict()

        time_now = datetime.now()
        timedelta_now = timedelta(hours=time_now.hour, minutes=time_now.minute)
        schedule_water_list = my_file['water']
        schedule_light_list = my_file['lights']

        result = []
        temp1, temp2 = {}, {}


        for schedule in schedule_water_list:

            temp1['type'], temp2['type'] = 'water', 'water'
            temp1['action'], temp2['action'] = 'on', 'off'
            temp1['timetable'] = datetime.strptime(schedule[0], '%H:%M:%S')
            temp2['timetable'] = datetime.strptime(schedule[1], '%H:%M:%S')
            result.extend([temp1, temp2])
            temp1, temp2 = {}, {}
        
        for schedule in schedule_light_list:

            temp1['type'], temp2['type'] = 'light', 'light'
            temp1['action'], temp2['action'] = 'on', 'off'
            temp1['timetable'] = datetime.strptime(schedule[0], '%H:%M:%S')
            temp2['timetable'] = datetime.strptime(schedule[1], '%H:%M:%S')
            result.extend([temp1, temp2])
            temp1, temp2 = {}, {}

        minimum, diff = None, None
        final_array = []

        for elm in result:
            timedelta_elm = timedelta(hours=elm['timetable'].hour, minutes=elm['timetable'].minute)
            
            if timedelta_elm == timedelta_now:
                final_array.append(elm)

        return final_array