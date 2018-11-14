import pandas as pd


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

excel_to_df('ExempleCROPS.xlsx')
