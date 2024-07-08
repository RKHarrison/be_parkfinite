import pytest
from api.utils.date_stamp import date_stamp
from api.utils.test_utils import is_valid_date


@pytest.mark.test_utils
class TestDateStampUtil:

    def test_date_stamp_format(self):
        test_stamp = date_stamp()
        assert is_valid_date(test_stamp) == True

    def test_date_stamp_updates(self):
        test_stamp1 = date_stamp()
        test_stamp2 = date_stamp()
        assert test_stamp1 != test_stamp2
