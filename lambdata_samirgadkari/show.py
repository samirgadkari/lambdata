import pandas as pd
from minepy import MINE

class Show:
    """ Show information in a useful way."""

    def __init__(self):
        return

    def nulls(self, df):
        """
        Show the count of nulls for each feature.
        """
        ns = pd.DataFrame(df.isnull().sum())
        return ns.rename({0: 'Nulls'}, axis=1)

    def corr(self, df, target_col_name):
        correlations = { 'pearson': df.corr(method = 'pearson'),
                         'kendall': df.corr(method = 'kendall'),
                         'spearman': df.corr(method = 'spearman') }
        res = pd.DataFrame({'pearson' + '-' + target_col_name: correlations['pearson'][target_col_name],
                            'kendall' + '-' + target_col_name: correlations['kendall'][target_col_name],
                            'spearman' + '-' + target_col_name: correlations['spearman'][target_col_name]}) \
                .T
        return res

    def mic(self, df, target_col_name):
        mine = MINE()
        cols = df.columns

        df2 = pd.DataFrame()
        for col in cols:
            if col == target_col_name:
                continue

            mine.compute_score(df[col], df[target_col_name])
            df2[col] = [mine.mic()]

        return df2.rename({0: 'MIC' + '-' + target_col_name}, axis = 0)

    def all(self, df, target_col_name):
        """
        Show nulls and describe outputs together
        """

        def create_dict(df, ns):
            """
            Create a mapping dictionary between the column names
            of ns and the column names of df.
            This makes it easier to append the two dataframes.
            """
            in_cols = ns.columns
            out_cols = df.columns

            if len(in_cols) != len(out_cols):
                print("Num columns in the two dataframes don't match up")
                return None

            d = {}
            for i in range(len(in_cols)):
                d[in_cols[i]] = out_cols[i]

            return d

        describe = df.describe()

        # Transpose creates the same kind of shape that we need
        # to append to the describe dataframe.
        ns = pd.DataFrame(self.nulls(df).values.flatten()).T

        # Renaming the dataframe with null counts to match
        # the result we need.
        ns = ns.rename(create_dict(df, ns), axis=1)
        ns = ns.rename({0: 'Nulls'})

        res = describe.append(ns)

        res = res.append(self.corr(df, target_col_name))
        res = res.append(self.mic(df, target_col_name))
        return res
