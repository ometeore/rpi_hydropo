# les fonctions restant à tester ici (et les motifs qui font qu'elles ne le sont pas):

# 	2   class myWebSocketApp

# 		on_open 	start le thread de la ws, lance en séparé tt les 60s nominal() Pourrai etre interessant

# 		__init__    super init l'héritage depuis websocket.WebSocketApp
# 					ajoute la propriété self.rpi (supposé prendre en paramètre un objet rpi)

# 		on_error	just make print
# 		on_close 	just make print

# 		on_open 	start le thread de la ws, lance en séparé tt les 60s nominal()

# 		manual_mode call everything off
# 					call get_task_done

from unittest import mock
from freezegun import freeze_time
from unittest.mock import patch, MagicMock, PropertyMock
from classes.use_file import Use_file
from classes import rpi

import json


@mock.patch.object(rpi, "get_task_done")
@freeze_time("2012-01-14 13:00:00")
def test_nominal(cls):
    fake_task = [{"type": "water", "action": "off"}]
    with patch.object(Use_file, "find_task", return_value=fake_task):
        rpi.nominal()
        cls.assert_called_once()


@mock.patch.object(rpi.MyWebSocketApp, "run_forever")
def test_ecoute(self):
    fake_dict = {"url": "on", "water": "off"}
    with patch.object(Use_file, "file_to_dict", return_value=fake_dict):
        my_rpi = rpi.Rpi()
        my_rpi.ecoute()
        self.assert_called_once()


@patch("time.sleep", return_value=None)
@mock.patch.object(rpi, "manual_mode")
def test_on_message(ignore_time_sleep, manual_mode):
    my_rpi = rpi.Rpi()
    my_ws = rpi.MyWebSocketApp(my_rpi, "url")

    result1 = MagicMock(
        side_effect=[
            {"message": {"message": {"manual": False}}},
            {"message": {"message": {"manual": True, "tool": "water"}}},
        ]
    )

    with patch("json.loads", result1):
        with patch.object(Use_file, "write_dico") as ok:
            rpi.on_message(my_ws, ["overwrite by patch json"])
            ok.assert_called_once()

        rpi.on_message(my_ws, ["overwrite by patch json"])
        manual_mode.assert_called_once()


@mock.patch.object(rpi, "get_task_done")
@mock.patch.object(rpi, "turn_everything_off")
def test_manual_mode(turn_off, get_task):
    rpi.manual_mode({"type": "water", "action": "off"})
    get_task.assert_called_once_with({"type": "water", "action": "off"})
    turn_off.assert_called_once()
