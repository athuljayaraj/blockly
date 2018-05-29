df = None
dataset = None
model_def = None
model = None
result = None

from reader import CsvReader
from model import ModelBuilder
from dataloader import DataSet
from sklearn import datasets
import numpy as np


if __name__ == "__main__":

  X = np.sort(100 * np.random.rand(2082, 8), axis=0)

  y = np.sin(X[:,0]).ravel()

  ###############################################################################
  # Add noise to targets
  #y[::5] += 3 * (0.5 - np.random.rand(8))
  print (X.shape,X)
  print (y.shape,y)

  dataset = (X,y,X,y)

  model = ModelBuilder.create_model('SVM Regression', config='{"keranal":"linear","c":1,"gamma":1}')
  model = ModelBuilder.train_model(model, dataset, 'true')

  df = CsvReader.read_csv("data","NSE_Abbott India Limited.csv",config="default",streamType="csv",columns="")
  dataset = DataSet.shape_data_frame(df,'',x_columns='1:9',y_columns='3',x_dimention='2',y_dimention='1',y_offset='1')
  print (dataset[0].shape)
  print(dataset[0])
  print (dataset[1].shape)
  print(dataset[1])

  model = ModelBuilder.create_model('SVM Regression', config='{"keranal":"linear","c":1,"gamma":1}')
  model = ModelBuilder.train_model(model, dataset, 'true')

  '''print (dataset[0].shape)
  #model_def = ModelBuilder.create_model('Gradient Boosting Regressor',config='{"random_state":0}')'''

  #result = ModelBuilder.predict_model(model,dataset)
