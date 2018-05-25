
import numpy as np


def shape_data_frame(xdf,ydf,x_columns=None,y_columns=None,x_dimention=2,y_dimention=1,y_offset =0):

    ydf = ydf if ydf else xdf
    numpy_matrix = ydf.as_matrix()
    ycol = get_array_from_string(y_columns)
    yarray = numpy_matrix[:,ycol] if ycol else numpy_matrix

    x_array = xdf.as_matrix()
    if x_columns :
        x_col_array = get_array_from_string(x_columns,separator=":") if ":" in x_columns else get_array_from_string(x_columns)
        x_array = x_array[:, x_col_array[0]:x_col_array[1]] if ":" in x_columns else x_array[:,x_col_array]

    if y_offset :
        y_offcet = int (y_offset)
        x_array = np.delete(x_array.copy(), np.s_[x_array.shape[0] - y_offcet:x_array.shape[0]],axis=0)
        yarray = np.delete(yarray.copy(), np.s_[0:y_offcet], axis=0)

    return x_array.astype(float),yarray.astype(float),x_array.astype(float),yarray.astype(float)


def get_array_from_string(input_string,separator=',') :
    array =[]
    if input_string :
        array = [int(x) for x in input_string.split(separator)]
    return array