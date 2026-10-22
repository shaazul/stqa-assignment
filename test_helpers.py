
from datetime import date, datetime, timedelta

from helpers import (
    compute_urgency,
    is_valid_password,
    is_valid_username,
    completed_in_last_n_days,
)


# WB-URG: Tests for compute_urgency

def test_urg_01_no_due_date():
    assert compute_urgency(None, today=date(2026, 10, 19)) == "No due date"


def test_urg_02_past_due_date():
    assert compute_urgency("2026-10-18", today=date(2026, 10, 19)) == "Overdue"


def test_urg_03_due_today():
    assert compute_urgency("2026-10-19", today=date(2026, 10, 19)) == "Due Today"


def test_urg_04_due_in_two_days():
    assert compute_urgency("2026-10-21", today=date(2026, 10, 19)) == "Due Soon"


def test_urg_05_due_in_three_days():
    assert compute_urgency("2026-10-22", today=date(2026, 10, 19)) == "Upcoming"


# WB-PWD: Tests for is_valid_password

def test_pwd_01_wrong_type():
    assert is_valid_password(None) is False


def test_pwd_02_seven_characters():
    assert is_valid_password("abc1234") is False


def test_pwd_03_eight_characters():
    assert is_valid_password("abc12345") is True


def test_pwd_04_nine_characters():
    assert is_valid_password("abc123456") is True


# WB-USER: Tests for is_valid_username

def test_user_01_wrong_type():
    assert is_valid_username(None) is False


def test_user_02_two_characters():
    assert is_valid_username("ab") is False


def test_user_03_three_characters():
    assert is_valid_username("abc") is True


def test_user_04_twenty_characters():
    assert is_valid_username("abcdefghijklmnopqrst") is True


def test_user_05_twenty_one_characters():
    assert is_valid_username("abcdefghijklmnopqrstu") is False


def test_user_06_underscore_allowed():
    assert is_valid_username("user_01") is True


def test_user_07_space_disallowed():
    assert is_valid_username("user name") is False


def test_user_08_hyphen_disallowed():
    assert is_valid_username("user-name") is False


# WB-DAY: Tests for completed_in_last_n_days

def test_day_01_missing_value():
    assert completed_in_last_n_days(
        None, n=7, now=datetime(2026, 10, 19, 12, 0, 0)
    ) is False


def test_day_02_recent_completion():
    assert completed_in_last_n_days(
        "2026-10-18 12:00:00",
        n=7,
        now=datetime(2026, 10, 19, 12, 0, 0),
    ) is True


def test_day_03_exactly_seven_days_ago():
    assert completed_in_last_n_days(
        "2026-10-12 12:00:00",
        n=7,
        now=datetime(2026, 10, 19, 12, 0, 0),
    ) is True


def test_day_04_future_completion():
    assert completed_in_last_n_days(
        "2026-10-20 12:00:00",
        n=7,
        now=datetime(2026, 10, 19, 12, 0, 0),
    ) is False


def test_day_05_completed_now():
    assert completed_in_last_n_days(
        "2026-10-19 12:00:00",
        n=7,
        now=datetime(2026, 10, 19, 12, 0, 0),
    ) is False


def test_day_06_older_than_seven_days():
    assert completed_in_last_n_days(
        "2026-10-11 12:00:00",
        n=7,
        now=datetime(2026, 10, 19, 12, 0, 0),
    ) is False


def test_urg_06_uses_current_date_when_today_not_provided():
    from datetime import date, timedelta

    tomorrow = (date.today() + timedelta(days=1)).strftime("%Y-%m-%d")

    assert compute_urgency(tomorrow) == "Due Soon"


def test_day_07_uses_current_time_when_now_not_provided():
    from datetime import datetime, timedelta

    recent_completion = (
        datetime.now() - timedelta(days=1)
    ).strftime("%Y-%m-%d %H:%M:%S")

    assert completed_in_last_n_days(recent_completion) is True
