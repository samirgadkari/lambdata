#!/usr/bin/env python
import unittest
import pandas as pd
import numpy as np
from show import Show


class ShowTest(unittest.TestCase):

    def test_nulls(self):
        df = pd.DataFrame({'col1': [11, 2, 3, 4, np.nan, np.nan],
                           'col2': [8, 9, 10, 11, 12, 13],
                           'col3': [3, 2, 1, 5, 6, 3]})
        res = Show().nulls(df).equals(pd.DataFrame(
                                        {'Nulls': [2, 0, 0]},
                                        index=['col1', 'col2', 'col3']))
        self.assertEqual(res, True)


if __name__ == '__main__':
    unittest.main()
