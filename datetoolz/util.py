import re
import datetime
import pyparsing as pp

def parse_text(text: str):
    """
    text: natural-number* space* unit 
    unit: week | day | hour | minute | seconds | microseconds | dayofweek | holiday  
    dayofweek: Mon-Sun
    holiday: easter
    >>> parser("10 days")
    (10, 'days')
    """
    assert type(text) == str, "supplied none string"
    space = pp.Literal(" ").suppress()
    ptrn = pp.Group(pp.ZeroOrMore(pp.Word(pp.nums))) + pp.ZeroOrMore(space) + \
        pp.Group(pp.Word(pp.alphas)) + pp.ZeroOrMore(space)
    n, unit = ptrn.parseString(text)
    n = int(n[0]) if n else 1.0
    unit = unit[0] 
    if not unit.endswith("s"): unit += 's'
    # assert unit in ('days', 'seconds', 'microseconds', 'milliseconds', 'minutes', 'hours', 'weeks')
    return n, unit


def parse_date(x, format):
    ptrn = r"(?:-|\s|T|:|\/)\s*"
    fields = re.split(ptrn, x)
    assert len(fields) >= 3
    year = int(fields[format.find("y")])
    month = int(fields[format.find("m")])
    day = int(fields[format.find("d")])
    fields += [0]*3 # add 0 for hour, minute and second if not present
    hour, minute, second = [int(x) for x in fields[3:6]]
    return datetime.datetime(year, month, day, hour, minute, second)
