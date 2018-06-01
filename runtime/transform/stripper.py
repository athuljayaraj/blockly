
def strip(columns, df):  # columns: list of columns numbers to be stripped
    try:
        results = list(map(int, columns))
    except:
        stripped_df = df.drop(columns, axis=1)
        return stripped_df
    return  df.drop(df.columns[results], axis=1)




import pandas as pd

if __name__ == '__main__':
    df1 = pd.DataFrame({'a': [1, 2, 3], 'b': [2, 3, 4]})
    dt = strip(columns='a'.split(','),df=df1)
    print(dt)