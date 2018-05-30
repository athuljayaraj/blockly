df = None
dataset = None
model_def = None
model = None
result = None

from reader import Reader
from model import ModelBuilder
from dataloader import DataSet
from sklearn import datasets
import numpy as np
from dataloader import Utils


if __name__ == "__main__":


  scaler_x = Utils.get_preprocessing_scaler(min_max_tuple=(-1, 1))
  #scaler_y = Utils.get_preprocessing_scaler(feature_range=(-1, 1))


  #X = np.sort(100 * np.random.rand(2082, 8), axis=0)

  #y = np.sin(X[:,0]).ravel()

  ###############################################################################
  # Add noise to targets
  #y[::5] += 3 * (0.5 - np.random.rand(8))
  # print (X.shape,X)
  #print (y.shape,y)

  #dataset = (X,y,X,y)

  #model = ModelBuilder.create_model('SVM Regression', config='{"keranal":"linear","c":1,"gamma":1}')
  #model = ModelBuilder.train_model(model, dataset, 'true')

  '''df = Reader.read_csv("data","NSE_Abbott India Limited.csv",config="default",streamType="csv",columns="")
  dataset = DataSet.shape_data_frame(df,'',x_columns='1:9',y_columns='3',x_dimention='3',y_dimention='1',y_offset='1')
  dataset = Utils.fit_transform(dataset,scaler_x)
  print (dataset[0].shape)
  print(dataset[1].shape)
  print (dataset[2].shape)
  print (dataset[3].shape)
  print (dataset[1])

  model = None'''

  dataframe = None
  shaper = None
  normalizer = None
  modelfef = None
  model = None
  result = None

  from reader import Reader
  from dataloader import DataSet
  from dataloader import Utils
  from model import ModelBuilder

  if __name__ == "__main__":
    dataframe = Reader.read_csv("data", "NSE_Abbott India Limited.csv", config="default", streamType="df",
                                   columns="")
    shaper = DataSet.shape_data_frame(dataframe, '', x_columns='1:9', y_columns='3', x_dimention='3', y_dimention='1',
                                      y_offset=1, test_data_size=20)
    normalizer = Utils.get_preprocessing_scaler(min_max_tuple=(-1, 1))
    shaper = Utils.fit_transform(shaper, normalizer)
    modelfef = ModelBuilder.create_model('Keras Sequential Model', shape='1,8', config=(
    '{"loss_function":"mean_absolute_error,"optimizer":"adam"}',
    ['{ "layer_type":"LSTM" ,"activation":"Tanh","optimizer":"Adam","threshold":"100","input_shape":"'1, 8'"}',
     '{ "layer_type":"Dropout" ,"activation":"sigmoid","optimizer":"sgd","threshold":".2","input_shape":""}',
     '{ "layer_type":"Dense" ,"activation":"linear","optimizer":"Adam","threshold":"1","input_shape":""}']))
    model = ModelBuilder.train_model(modelfef, shaper, 'true')
    result = ModelBuilder.predict_model(model, shaper)

  model = ModelBuilder.create_model('Sequential', config=('{"loss_function":"mean_squared_error","optimizer":"adam"}',
                                                          ['{"layer_type":"LSTM","threshold":"1000","activation":"tanh","input_shape":"'+str(dataset[0].shape[1])+','+str(dataset[0].shape[2])+'"}',
                                                           '{"layer_type":"Dropout","threshold":"0.2"}',
                                                           '{"layer_type":"Dense","threshold":1,"activation":"linear"}']))
  model = ModelBuilder.train_model(model, dataset, 'true')

  """
  print (dataset[0].shape)
  model_def = ModelBuilder.create_model('Gradient Boosting Regressor',config='{"random_state":0}')
  """

  result = ModelBuilder.predict_model(model,dataset)
  print(Utils.inverse_transform(result,scaler_x))




