import os
import re
import pandas


def csv_files_from_dir(folder):
    return [os.path.join(folder, f) for f in os.listdir(folder) if re.match(r'.*\.(csv)', f, flags=re.I)]


def get_input_files(input_path):
   return [file for file in csv_files_from_dir(input_path)]


def read_csv(dirPath,uri,columns = None,config = None,streamType =None) :
    if uri :
        file_path = os.path.join(dirPath, uri)
        df = pandas.read_csv(file_path)
        if(config != None):
            addColumnsToDF(df, config)
        return df
    else :
        df_collection = []
        for file in get_input_files(dirPath):
            df_collection.append(pandas.read_csv(file))
        return df_collection


def addColumnsToDF(df, config):
    columns = config.split(",")
    for column in columns:
        if column: #date, timestamp, folderName, fileName, constant string, constant int, sequence generator

    #     return df