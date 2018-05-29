import pandas as pd

def joiner(list_of_dfs):

    df_final = reduce(lambda left, right: pd.merge(left, right, on='name'), list_of_dfs)
