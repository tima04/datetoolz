from datetoolz.date import Date, date

class TestDate:
    pass

def test_date():
    x = Date("2018-01-10")
    assert type(x) == Date
    y = date("2018-01-10")
    assert x == y


def test_parse_date():
    x = Date("2018-01-10")
    y = Date("2018/01/10")
    # z = Date("01-10-2018T0:0:0")
    assert x == y

def test_add():
    x = Date("2018-01-10")
    y = x + '3 seconds'
    assert y > x


def test_sub():
    x = Date("2018-01-10")
    # y = x - '3month '
    y = x - '3days'
    assert y < x


def test_ymd_hms():
    x = Date("2018/01/10T10:20:0")
    # x = date("2018-01-10T10:20:0")
    assert x.year == 2018
    assert x.month == 1
    assert x.day == 10 
    assert x.hour == 10
    assert x.minute == 20
    assert x.second == 0
