import pandas as pd
import numpy as np


archivo_excel = 'datos.xlsx'


def bulk_data(hoja):
    
    dataframe = pd.read_excel(archivo_excel, hoja)

    header_titles = {}
    for column in dataframe.columns:
        header_titles[column] = 'a'

    header = pd.Series(header_titles)
    df = pd.concat([dataframe, header.to_frame().T]).replace(np.nan, None).iloc[:-1, :]


    bulk_data = []

    for index, col in df.iterrows():
        data = (col)
        bulk_data.append(data)

    return bulk_data