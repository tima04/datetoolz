import datetime
import re
import pyparsing as pp

class Date(object):

    def __init__(self, x, form="ymd"):
        "x datetime or string"
        assert type(x) in (str, datetime.datetime)
        assert set(form) == set("ymd")
        self.form = form
        self._dt = x if type(x) == datetime.datetime else self._parse_date(x)
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

    def _parse_date(self, x):
        form = self.form
        ptrn = r"(?:-|\s|T|:|\/)\s*"
        fields = re.split(ptrn, x)
        assert len(fields) >= 3
        year = int(fields[form.find("y")])
        month = int(fields[form.find("m")])
        day = int(fields[form.find("d")])
        fields += [0]*3 # add 0 for hour, minute and second if not present
        hour, minute, second = [int(x) for x in fields[3:6]]
        return datetime.datetime(year, month, day, hour, minute, second)

    def _totimedelta(self, arg):
        assert type(arg) in (str, datetime.timedelta)
        if type(arg) == datetime.timedelta:
            return arg
        n, unit = self._parse_arg(arg)
        return datetime.timedelta(**{unit: n})
        
    def _parse_arg(self, arg):
       "if int then may be as a day, or take option"
       assert type(arg) == str, "supplied none string"
       space = pp.Literal(" ").suppress()
       ptrn = pp.Group(pp.OneOrMore(pp.Word(pp.nums))) + pp.ZeroOrMore(space) + \
           pp.Group(pp.Word(pp.alphas)) + pp.ZeroOrMore(space)
       n, unit = ptrn.parseString(arg)
       n = float(n[0])
       unit = unit[0] 
       if not unit.endswith("s"): unit += 's'
       assert unit in ('days', 'seconds', 'microseconds',
                       'milliseconds', 'minutes', 'hours',
                       'weeks')
       return n, unit

    def todatetime(self):
        return self._dt


def date(x, form="ymd"):
    assert set(form) == set("ymd")
    return Date(x, form)
