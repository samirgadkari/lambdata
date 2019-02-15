# lambdata
Python package with helpful utility functions for DataScience!

# Current functionality
  - Shows the Null count for each column in a Dataframe
  - Shows the Pearson/Kendall/Spearman correlation coefficients
    for each feature against the target
  - Shows the MIC value for each feature against the target
  - Shows all of the above in one Dataframe output table

# Install
In Jupyter Notebook or from the command line:

!pip install -U --index-url https://test.pypi.org/simple/ lambdata-samirgadkari

# Usage
import lambdata_samirgadkari as s
  - s.show.nulls(df)
  - s.show.corr(df, target_col_name)
  - s.show.mic(df, target_col_name)
  - s.show.all(df, target_col_name)

# Future
  - Show scatterplots between each feature and the target
  - Show Variance Inflation Threshold values for each feature