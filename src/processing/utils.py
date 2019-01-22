import pandas as pd
from unidecode import unidecode


def excel_to_df(file_name, file_type):
    """
    Imports excel sheets for one data source into one DataFrame
    :param file_name: name of data source to use (in config.py)
    :param file_type: specify the type of file (helpers, data)
    :return: single DataFrame of excel data
    """
    file_path = f"./{file_type}/{file_name}"
    xlsx = pd.ExcelFile(file_path)
    sheet_names = xlsx.sheet_names

    data_df = pd.DataFrame()
    for sheet in sheet_names:
        data_df = data_df.append(pd.read_excel(file_path, sheet_name=sheet),
                                 ignore_index=True)
    columns = ["id",
               "datetime",
               "localisation",
               "comment"]
    data_df.set_axis(columns, axis='columns', inplace=True)
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


def get_acronym_dict():
    """
    Fetches the acronym dictionary from the helpers folder and formats it
    :return: a dictionary for converting acronyms to full terms
    """
    file_name = "dict_acronymes.xlsx"
    file_type = "helpers"
    df = excel_to_df(file_name, file_type)
    df = df[['Acronym', 'Term']].dropna()
    acronym_dict = df.set_index('Acronym').T.to_dict('records')[0]

    return acronym_dict


def replace_acronyms(text, acronym_dict):
    """
    Replaces acronyms in a text according to an acronym dictionary
    :param text: string to modify
    :param acronym_dict: dictionary of acronyms
    :return: the modified string
    """
    for key, value in acronym_dict.items():
        text.replace(key, value)

    return text


def replace_acronyms_df(df, column):
    """
    Replaces acronyms for a whole column of a DataFrame
    :param df: DataFrame to modify
    :param column: column to modify
    """
    acronym_dict = get_acronym_dict()
    df[column] = df[column].map(lambda x: replace_acronyms(x, acronym_dict))

    return df


def get_material_dict():
    """
    """
    file_name = "dict_materiel.xlsx"
    file_type = "helpers"
    df = excel_to_df(file_name, file_type)
    df = df[['Acronym', 'Term']].dropna()
    acronym_dict = df.set_index('Acronym').T.to_dict('records')[0]

    return acronym_dict
