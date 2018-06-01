import pandas as pd
import numpy as np

def concat(list_of_joiner_input):
    for joiner_input in list_of_joiner_input:
        joiner_input.get('csv')


# def join(list_of_joiner_input, style):
    # if (style == 'join' and len(list_of_joiner_input) > 1):
    #     for joiner_input in list_of_joiner_input[1:]:





def myfunc(x):
    return x+1

if __name__ == '__main__':
    # joiner.join([{"csv":, "key":1, "columns":"1"}, {"csv":, "key":1, "columns":"1"}, {"csv":, "key":1, "columns":"1"}], 'row')
    df = pd.DataFrame(np.random.randint(0, 100, size=(100, 4)), columns=list('ABCD'))
    tt = df.transform({'A': myfunc, 'B': lambda x: x})
    print(myfunc(10))
