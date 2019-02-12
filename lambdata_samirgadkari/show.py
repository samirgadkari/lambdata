import pandas as pd


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

    def all(self, df):
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
                return {}

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

        return describe.append(ns)
