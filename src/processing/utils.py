import pandas as pd
from unidecode import unidecode


def excel_to_df(file_name):
    """
    Imports excel sheets for one data source into one DataFrame
    :param data_source: name of data source to use (in config.py)
    :return: single DataFrame of excel data
    """
    file_path = f"./data/{file_name}"
    xlsx = pd.ExcelFile(file_path)
    sheet_names = xlsx.sheet_names

    data_df = pd.DataFrame()
    for sheet in sheet_names:
        data_df = data_df.append(pd.read_excel(file_path, sheet_name=sheet),
                                 ignore_index=True)

    return data_df


def remove_accents(df, column):
    """
    Removes accents of a column of a DataFrame
    :param df: DataFrame
    :param column: name of the column
    :return: the DataFrame
    """
    df[column] = df[column].map(lambda x: unidecode(x))

    return df


def remove_caps(df, column):
    """
    Removes accents of a column of a DataFrame
    :param df: DataFrame
    :param column: name of the column
    :return: the DataFrame
    """
    df[column] = df[column].str.lower()

    return df
