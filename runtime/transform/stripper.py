
def strip(columns, df):  # columns: list of columns numbers to be stripped
    columns = columns.split(',')
    for element in columns:
        [start,end] = element.split(':')
    try:
        results = list(map(int, columns))
    except:
        stripped_df = df.drop(columns, axis=1)
        return stripped_df
    return  df.drop(df.columns[results], axis=1)




import pandas as pd

if __name__ == '__main__':
    df1 = pd.DataFrame({'a': [1, 2, 3], 'b': [2, 3, 4], 'c': [4, 5, 6], 'd':[5, 6, 7]})
    dt = strip('0,1:3',df=df1)
    print(dt)

    x = '1,3:5,7,9,12:16'
    list = x.split(',')
    index = 0
    for element in list:
        try:
        [start,end] = element.split(':')
        for i in range(int(start),int(end)+1):
            list.index(start)
            list.insert()



