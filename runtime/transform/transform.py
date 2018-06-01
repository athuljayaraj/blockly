import custom_functions as cf

def get_function(function):
    if function.startswith('lambda'):
        return function
    else:
        return 'cf.'+function

def transform_df(df, transformers):
    begin = 'df.transform({'
    code = []
    for transformer in transformers:
        code.append('\''+str(transformer.get('column'))+'\': '+str(get_function(transformer.get('function'))))
    code = str(','.join(code))
    end = '})'
    code = ''.join([begin, code, end])
    dt = eval(code)
    return dt


import pandas as pd
import numpy as np

if __name__ == '__main__':
    df = pd.DataFrame(np.random.randint(0, 10, size=(5, 3)), columns=list('123'))
    dt = transform_df(df, [{"column": 1, "function": "lambda x:x+1"}, {"column": 2, "function": "plus1"},
                           {"column": 3, "function": "lambda x:x+3"}])
    print(dt)
