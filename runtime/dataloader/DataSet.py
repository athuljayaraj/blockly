
import numpy as np
from numpy import zeros, newaxis



def shape_data_frame(xdf,ydf,x_columns=None,y_columns=None,x_dimention=2,y_dimention=1,y_offset =0,test_data_size=20):

    ydf = ydf if ydf else xdf
    numpy_matrix = ydf.as_matrix()
    ycol = get_array_from_string(y_columns)
    yarray = numpy_matrix[:,ycol] if ycol else numpy_matrix

    x_array = xdf.as_matrix()
    if x_columns :
        x_col_array = get_array_from_string(x_columns,separator=":") if ":" in x_columns else get_array_from_string(x_columns)
        x_array = x_array[:, x_col_array[0]:x_col_array[1]] if ":" in x_columns else x_array[:,x_col_array]

    if y_offset:
        y_offcet = int (y_offset)
        x_array = np.delete(x_array.copy(), np.s_[x_array.shape[0] - y_offcet:x_array.shape[0]],axis=0)
        yarray = np.delete(yarray.copy(), np.s_[0:y_offcet], axis=0)
        yarray = yarray.ravel() if int(y_dimention) == 1 else yarray

    #x_array = scaler_x.fit_transform(x_array.astype(float))
    #yarray = scaler_y.fit_transform(yarray.astype(float))

    x_test = np.delete(x_array.copy(), np.s_[0: int(x_array.shape[0] * (1-float(test_data_size)/100))], axis=0)
    y_test = np.delete(yarray.copy(), np.s_[0: int(yarray.shape[0] * (1- float(test_data_size)/100))], axis=0)

    if int(x_dimention) ==3 :
        x_test = x_test[:, newaxis,:]
        x_array = x_array[:,newaxis,:]
    return x_array.astype(float),yarray.astype(float),x_test.astype(float),y_test.astype(float)


def get_array_from_string(input_string,separator=',') :
    array =[]
    if input_string :
        array = [int(x) for x in input_string.split(separator)]
    return array
