import os
import re
import pandas
import pickle


def csv_files_from_dir(folder):
    return [os.path.join(folder, f) for f in os.listdir(folder) if re.match(r'.*\.(csv)', f, flags=re.I)]


def get_input_files(input_path):
   return [file for file in csv_files_from_dir(input_path)]


def read_csv(dirPath,uri,columns = None,config = None, streamType =None,filter=None,count=1) :
    if uri :
        file_path = os.path.join(dirPath, uri)
        df = pandas.read_csv(file_path)
        df = df.head(count) if filter == 'head' else df.tail(count) if filter == 'tail' else df
        return df
    else :
        df_collection = []
        for file in get_input_files(dirPath):
            df = pandas.read_csv(file)
            df_collection.append(df.head(count) if filter == 'head' else df.tail(count) if filter == 'tail' else df)
        return df_collection

def add_columns_to_df(df, config, file_name, folder_name):
    columns = config.split(",")  # date, timestamp, folderName, fileName, constant string, constant int
    i = 0
    for column in columns:
        i = i+1
        column_value = f(column)
        if not column_value:
            column_value = get_value(column)
        df['__ec' + i] = column_value
    return df


def f(x):
    return {
        'date': dt.datetime.now().date(),
        'timestamp': dt.datetime.now(),
        'folderName': __folderName,
        'fileName': __fileName
    }.get(x, None)


def get_value(s):
    try:
        return float(s)
    except ValueError:
        return s

'''
Load trained model from disk 
'''
def read_model(file_path):
    model = None
    if file_path is not None:
        with open(file_path, 'rb') as f:
            model = pickle.load(f)
    return model







