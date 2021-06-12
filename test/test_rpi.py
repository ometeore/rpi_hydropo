# les fonctions restant à tester ici (et les motifs qui font qu'elles ne le sont pas):

# 	1	class rpi

# 		__init__    assez inutile 

# 		ecoute      va recuperer l'url d'un serveur depuis un fichier
# 					instencie myWebSocketApp(une version hérité de WebsocketApp de la lib websocket-client)
# 					lui associe on_open
# 					lance la methode run_forever

# 	2   class myWebSocketApp
 
# 		__init__    super init l'héritage depuis websocket.WebSocketApp
# 					ajoute la propriété self.rpi (supposé prendre en paramètre un objet rpi)

# 		on_error	just make print
# 		on_close 	just make print

# 		on_open 	start le thread de la ws, lance en séparé tt les 60s nominal()

# 		nominal		mock the return of Use_file.find task
#                   -> return [{'type': 'water', 'action': 'off', 'timetable': datetime.datetime(1900, 1, 1, 15, 30)}]
#                   because of freezegun it will call one time get_task_done


# 		manual_mode call everything off
# 					call get_task_done 

from unittest import mock
from freezegun import freeze_time
from unittest.mock import patch, MagicMock, PropertyMock
from classes.use_file import Use_file
from classes import rpi 


class Use_file_task_return():
    pass

@mock.patch.object(rpi, 'get_task_done' )
@freeze_time("2012-01-14 13:00:00")
def test_nominal(blyat):
    fake_task = [{'type': 'water', 'action': 'off'}]
    with patch.object(Use_file, 'find_task', return_value=fake_task):
        rpi.nominal()
        blyat.assert_called_once()
