# df2 = pd.DataFrame({'col1': [pd.Timestamp.now()]})
# res = datetime.day(df2['col1'])
# Gives res:
# 0    Friday
# Name: col1.  dtype: object

# df = pd.DataFrame({'col1': ['2017-12-12', '2016-01-01']})
# res = datetime.day(df['col1'])
# 0    Tuesday
# 1     Friday
# Name: col1, dtype: object
