from unittest import mock
from freezegun import freeze_time
from unittest.mock import patch, MagicMock, PropertyMock, Mock
from classes.use_file import Use_file
from classes import demonstration

def test_ph_mesure():
    fake_dict = {"ph": 7}
    with patch.object(Use_file, "file_to_dict", return_value=fake_dict):
        assert 6 <= demonstration.ph_mesure() <= 8


def test_ec_mesure():
    fake_dict = {"ec": 1500}
    with patch.object(Use_file, "file_to_dict", return_value=fake_dict):
        assert 1470 <= demonstration.ec_mesure() <= 1530