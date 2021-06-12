import pytest
import io
import datetime
from freezegun import freeze_time
from unittest.mock import mock_open, patch, MagicMock, PropertyMock
from classes.use_file import Use_file


# def Mock_file(self):
#     class Test(_io.TextIOWrapper):  ### Test(file)
#         def __init__(self):
#             self.mode = 'w'
#     return Test()

def test_file_to_dict():
    """get the file of name self.path (self is frome Usefile object) and return the json inside"""
    #recupere le fichier et retourne un objet dict
    # patch with open et return un type dict (ou json maybe)
    with patch('builtins.open', mock_open(read_data='{"manual": false}')):
        test = Use_file('my_file.txt')
        test_dict = test.file_to_dict()
        assert type(test_dict) is dict
        assert test_dict['manual'] == False


@freeze_time("2012-01-14 13:00:00")
def test_find_task():
    """ 1 mock file_to_dict to get a dict of schedule
        2 mock a datetime (we use freezgun module here)
        3 check if return list of task(s)
        NB: example of task is : {'type': 'water', 'action': 'off', 'timetable': datetime.datetime(1900, 1, 1, 15, 21)}
    """
    fake_schedule = {"water": [["13:03:00", "13:00:00"]], "lights": [["13:09:00", "13:10:00"]]}
    my_file = Use_file('my_file.txt')
    my_file.file_to_dict = MagicMock(return_value=fake_schedule)
    result_array = my_file.find_task()
    assert result_array[0]['type'] == "water"
    assert len(result_array) == 1

class MockFile:
    def open(self, *args, **kwargs):
        return io.StringIO()

def test_write_dico(tmpdir):
    """ write a python dict inside and file deleting what was previously inside"""
    pass
    # my_temp_file_path = tmpdir.join('output.txt')

    # with patch(Use_file, new_callable=PropertyMock) as mock_my_property:
    #     mock_my_property.return_value = my_temp_file_path
    #     my_file = Use_file("txt")
    #     print(my_file.path)