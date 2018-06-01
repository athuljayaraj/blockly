
def strip(columns, df):  # columns: list of columns numbers to be stripped
    stripped_df = df.drop(df.columns[columns], axis=1)
    return stripped_df
