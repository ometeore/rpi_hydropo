from unittest import mock
from freezegun import freeze_time
from unittest.mock import patch, MagicMock, PropertyMock
from classes.use_file import Use_file
from classes import rpi
from classes import demonstration as demo

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


##########  DONT WORK, DONT KNOW WHY, it s the same as above...


# @mock.patch.object(demo, "water_stop")
# def test_turn_everything_off(water_stop):
#     rpi.turn_everything_off()
#     water_stop.assert_called_once()
    

# def turn_everything_off():
#     water_stop()
#     light_stop()
#     conduct_stop()
#     ph_stop()



# @mock.patch.object(rpi, "get_task_done")
# @mock.patch.object(rpi, "turn_everything_off")
# def test_send_status():
#     fake_dict = {"rpi_name": "name_rpi"}
#     with patch.object(Use_file, "file_to_dict", return_value=fake_dict):
#         #with patch 
#         test_result = rpi.send_status()
#         assert test_result == "blyat"

# def send_status():
#     """get ph and ec from hardware and prepare a message to send"""

#     my_file = Use_file("settings.txt")
#     dict_settings = my_file.file_to_dict()

#     message_to_send = {}
#     message_to_send["rpi_name"] = dict_settings["rpi_name"]
#     message_to_send["ph"] = ph_mesure()
#     message_to_send["ec"] = ec_mesure()

#     print(message_to_send)
#     return message_to_send

def test_get_task_done():
    pass

# def get_task_done(task):
#     if task['type'] == 'water':
#         if task['action'] == 'on':
#             led_blue_start()
#             water_start()
#         if task['action'] == 'off':
#             led_blue_stop()
#             water_stop()
#     if task['type'] == 'light':
#         if task['action'] == 'on':
#             led_yellow_start()
#             light_start()
#         if task['action'] == 'off':
#             light_stop()
#             led_yellow_stop()
