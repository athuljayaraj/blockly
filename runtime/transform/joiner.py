from functools import reduce
import pandas as pd
import numpy as np

def concat(list_of_joiner_input):
    for joiner_input in list_of_joiner_input:
        joiner_input.get('csv')


def join(list_of_joiner_input, style):
    df = None
    if style == 'join':
        df = reduce(lambda left, right: pd.merge(left.get('csv'), right.get('csv'), left_on=left.get('column'),
                                                       right_on=right.get('column')), list_of_joiner_input)
    return df


import pandas as pd
import numpy as np

if __name__ == '__main__':
    df1 = pd.DataFrame({'a': [1, 2, 3], 'b': [2, 3, 4]})
    df2 = pd.DataFrame({'a': [1, 2, 3], 'c': [4, 7, 9]})
    dt = join([{"csv":df1,"key":'a',"columns":"1,2,3"}, {"csv":df2,"key":'a',"columns":"1,2,3"}],'join')
    print(dt)
