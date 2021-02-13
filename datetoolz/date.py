import datetime
from datetoolz.util import parse_text, parse_date

class Date(object):
    def __init__(self, x, format="ymd"):
        "x datetime or string"
        assert type(x) in (str, datetime.datetime)
        assert set(format) == set("ymd")
        self.format = format
        self._dt = x if type(x) == datetime.datetime else parse_date(x, format)
        self.year = self._dt.year
        self.month = self._dt.month
        self.day = self._dt.day
        self.hour = self._dt.hour
        self.minute = self._dt.minute
        self.second = self._dt.second
        
    def __str__(self):
        return self._dt.strftime("%Y-%m-%d")

    def __repr__(self):
        return self._dt.strftime("%Y-%m-%d")

    def __add__(self, arg):
        rslt = self._dt + self._totimedelta(arg)
        return Date(rslt)

    def __sub__(self, arg):
        rslt = self._dt - self._totimedelta(arg)
        return Date(rslt)

    def __gt__(self, other):
       return self._dt > other.todatetime()

    def __lt__(self, other):
       return self._dt < other.todatetime()

    def __eq__(self, other):
       return self._dt == other.todatetime()

    def _totimedelta(self, arg):
        assert type(arg) in (str, datetime.timedelta)
        if type(arg) == datetime.timedelta:
            return arg
        n, unit = parse_text(arg)
        return datetime.timedelta(**{unit: n})
        
    def todatetime(self):
        return self._dt


def date(x, format="ymd"):
    assert set(format) == set("ymd")
    return Date(x, format)
