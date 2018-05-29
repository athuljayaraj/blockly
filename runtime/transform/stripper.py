import pandas

def strip(columns, df):
    stripped_df = df.drop(df.columns[columns], axis=1)
    return stripped_df
