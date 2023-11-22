import datetime
from functools import reduce


def now14() -> str:
    return reduce(lambda x, y: str(x).zfill(2) + str(y).zfill(2), datetime.datetime.now().timetuple()[:6])
