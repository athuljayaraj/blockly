df = None
dataset = None
model_def = None
model = None
result = None


from reader import CsvReader
from model import ModelBuilder
from dataloader import DataSet

if __name__ == "__main__" :

  df = CsvReader.read_csv("data","NSE_Abbott India Limited.csv",config="default",streamType="csv",columns="")
  dataset = DataSet.shape_data_frame(df,'',x_columns='1:9',y_columns='2,3',x_dimention='2',y_dimention='1',y_offset='1')
  model_def = ModelBuilder.create_model('Gradient Boosting Regressor',config='{"random_state":0}')
  model = ModelBuilder.train_model(model_def,dataset,'true')
  result = ModelBuilder.predict_model(model,dataset)
