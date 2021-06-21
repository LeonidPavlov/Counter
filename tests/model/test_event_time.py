from datetime import datetime as dt

from counter.model.event_time import Event_Time



def test_check_year_out_of_range_minus() -> None:
    assert(Event_Time.check_year_out_of_range(0) == dt.now().year)

def test_check_year_out_of_range_plus() -> None:
    assert(Event_Time.check_year_out_of_range(10000) == dt.now().year)

def test_check_year_out_of_range_normal() -> None:
    assert(Event_Time.check_year_out_of_range(dt.now().year) == dt.now().year)

def test_check_month_out_of_range_minus() -> None:
    assert(Event_Time.check_month_out_of_range(0) == dt.now().month)

def test_check_month_out_of_range_plus() -> None:
    assert(Event_Time.check_month_out_of_range(13) == dt.now().month)

def test_check_month_out_of_range_normal() -> None:
    assert(Event_Time.check_month_out_of_range(dt.now().month) == dt.now().month)



def test_Event_Time_year_default_parameter() -> None:
    assert (Event_Time().event_year() == dt.now().year)

def test_Evemt_Time_year_arbitrary_parameter1() -> None:
    assert (Event_Time(year = 2033).event_year() == 2033)

def test_Event_Time_month_arbitrary_parameter2() -> None:
    assert( Event_Time(month = 7).event_month() == 7)


def test_is_leap1() -> None:
    assert (Event_Time.is_leap(2000) == True)

def test_is_leap2() -> None:
    assert (Event_Time.is_leap(1835) == False)

def test_is_leap3() -> None:
    assert (Event_Time.is_leap(2020) == True)

def test_is_leap4() -> None:
    assert (Event_Time.is_leap(2033) == False)

def test_hour_out_of_range_plus() -> None:
    assert(Event_Time.chek_hour_out_of_range(24) == dt.now().hour)

def test_hour_out_of_range_minus() -> None:
    assert(Event_Time.chek_hour_out_of_range(-1) == dt.now().hour)

def test_hour_out_of_range_argitrary() -> None:
    assert(Event_Time.chek_hour_out_of_range(14) == 14)

def test_minute_out_of_range_mius() -> None:
    assert(Event_Time.chek_minute_out_of_range(-1) == dt.now().minute)

def test_minute_out_of_range_plus() -> None:
    assert(Event_Time.chek_minute_out_of_range(60) == dt.now().minute)

def test_hour_out_of_range_argitrary() -> None:
    assert(Event_Time.chek_minute_out_of_range(45) == 45)


def test_chek_day_in_month_out_of_range_minus() -> None:
    assert (Event_Time.chek_amount_days(2030,2,0) == dt.now().day)

def test_chek_day_in_month_out_of_range_plus() -> None:
    assert (Event_Time.chek_amount_days(2045,1,32) == dt.now().day)

def test_chek_day_in_month_february_leap() -> None:
    assert(Event_Time.chek_amount_days(2020, 2, 29) == 29)

def test_chek_day_in_february_arbitrary_year() -> None:
    assert(Event_Time.chek_amount_days(2021, 2, 29) == dt.now().day)

date = Event_Time(2032, 7, 14, 23, 45)

def test_event_year_arbitray_value() -> None:
    assert(date.event_year() == 2032)

def test_event_month_arbitray_value() -> None:
    assert(date.event_month() == 7)

def test_event_day_arbitray_value() -> None:
    assert(date.event_day() == 14)

def test_event_hour_arbitray_value() -> None:
    assert(date.event_hour() == 23)

def test_event_minute_arbitray_value() -> None:
    assert(date.event_minute() == 45)

