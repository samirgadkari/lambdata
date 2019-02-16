import pandas as pd

class DateTime:
    """Manipulate Date-Time columns into useful information"""

    def __init__(self):
        return

    def get_dt(self, col, kwargs):
        if len(col) == 0:
            return None

        if isinstance(col[0], str):
            dt = pd.to_datetime(col, **kwargs)
            res = pd.Series(dt)
            return res
        elif isinstance(col[0],
                        pd._libs.tslibs.timestamps.Timestamp):
            dt = pd.Series(col)
            return dt
        else:
            raise ValueError(
                  "Cannot find DateTime for " +
                    str("type " + str(type(col[0])))
                      if len(col) > 0 else "unknown type")

        return None

    def day(self, col, **kwargs):

        return self.get_dt(col, kwargs).dt.weekday_name

    def month(self, col, **kwargs):

        return self.get_dt(col, kwargs).dt.month

    def year(self, col, **kwargs):

        return self.get_dt(col, kwargs).dt.year
