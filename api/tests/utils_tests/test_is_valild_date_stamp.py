import pytest
from utils.test_utils import is_valid_date


@pytest.mark.test_utils
class TestIsValidDateUtil:

    def test_empty_input(self):
        assert is_valid_date("") == False
        assert is_valid_date(None) == False

    def test_valid_iso(self):
        assert is_valid_date("2024-07-03T13:40:45.657629") == True

    def test_invalid_iso_strin(self):
        assert is_valid_date("INVALID") == False

    def test_invalid_data_types(self):
        assert is_valid_date(1) == False
        assert is_valid_date(1.234) == False
        assert is_valid_date({}) == False
        assert is_valid_date(["2024-07-03T13:40:45.657629"]) == False
