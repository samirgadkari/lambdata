import pandas as pd
from minepy import MINE
from statsmodels.stats.outliers_influence import variance_inflation_factor


class Show:
    """ Show information in a useful way."""

    def __init__(self):
        return

    def nulls(self, df):
        """
        Return the count of nulls for each feature.
          Parameters:
            df: DataFrame
          Returns:
            DataFrame that contains null count of each column.
        """
        ns = pd.DataFrame(df.isnull().sum())
        return ns.rename({0: 'Nulls'}, axis=1)

    def corr(self, df, target_col_name):
        """
        Return the Perason/Kendall/Spearman correlations
        for each feature.
          Parameters:
            df: DataFrame
          Returns:
            Dataframe containing the correlations for each feature.
        """
        correlations = {
            'pearson': df.corr(method='pearson'),
            'kendall': df.corr(method='kendall'),
            'spearman': df.corr(method='spearman')
        }
        s = '-' + target_col_name
        res = pd.DataFrame({'pearson' + s:
                            correlations['pearson'][target_col_name],
                            'kendall' + s:
                            correlations['kendall'][target_col_name],
                            'spearman' + s:
                            correlations['spearman'][target_col_name]}) \
                .T
        return res

    def mic(self, df, target_col_name):
        """
        Perform MIC calculations for each feature, except the target feature.
        Return the calculation values in a Dataframe.
          Parameters:
            df: DataFrame
            target_col_name: String containing name of target
          Returns:
            Dataframe containing the MIC calculations for each feature,
            against the target feature.
        """
        mine = MINE()
        cols = df.columns

        df2 = pd.DataFrame()
        for col in cols:
            if col == target_col_name:
                continue

            mine.compute_score(df[col], df[target_col_name])
            df2[col] = [mine.mic()]

        return df2.rename({0: 'MIC' + '-' + target_col_name}, axis=0)

    def VIF(self, df):
        """
        Calculate the Variance Inflation Factor (VIF)
          Parameters:
            df: Dataframe
          Returns:
            Returns a dataframe with the VIF in it.
        """
        res = pd.DataFrame(
                {'VIF': [variance_inflation_factor(df.values, i)
                         for i in range(df.shape[1])]},
                index=df.columns)
        return res.T

    def all(self, df, target_col_name):
        """
        Show null count, describe output, correlation,
        and MIC calculations together.
          Parameters:
            df: Dataframe
            target_col_name: String containing name of target
          Returns:
            Dataframe containing:
              - null counts for each feature,
              - describe output for each numerical feature,
              - correlation coefficients for each numerical feature,
              - MIC calculations for each numerical feature.
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
        res = res.append(self.VIF(df))
        return res
