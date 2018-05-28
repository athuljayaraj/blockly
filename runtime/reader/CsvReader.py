import os
import re
import pandas
import datetime as dt


__folderName = ''
__fileName = ''


def csv_files_from_dir(folder):
    return [os.path.join(folder, f) for f in os.listdir(folder) if re.match(r'.*\.(csv)', f, flags=re.I)]


def get_input_files(input_path):
    return [file for file in csv_files_from_dir(input_path)]


def read_csv(dir_path, uri, columns=None, config=None, stream_type=None):
    if uri:
        file_path = os.path.join(dir_path, uri)
        df = pandas.read_csv(file_path)

        if not config:
            add_columns_to_df(df, config, file_name, folder_name )
        return df
    else:
        df_collection = []
        for input_file in get_input_files(dir_path):
            df_collection.append(pandas.read_csv(input_file))
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
