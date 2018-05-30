import pandas
import pickle

def write_csv(data_frame,out_file_name):
    data_frame.writecsv(out_file_name)

'''
write trained model to disk
'''
def write_model(model,out_file_path,regx = None):
   if out_file_path  is not None:
    with open(out_file_path, 'wb') as f:
        pickle.dump(model, f)