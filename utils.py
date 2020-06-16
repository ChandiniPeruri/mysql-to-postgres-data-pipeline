import pandas as pd


""" get_tables method returns tables from the table list file
    parameter: string
    return: list
"""


def get_tables(path):
    tables = pd.read_csv(path, sep=':')
    return tables.query('to_be_loaded == "yes"')
