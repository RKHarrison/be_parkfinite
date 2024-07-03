from datetime import datetime

def is_valid_date(date_str):
    if not date_str or type(date_str) != str:
        return False
    try:
        datetime.fromisoformat(date_str)
        return True
    except ValueError:
        return False