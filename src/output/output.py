import pandas as pd

def df_to_excel(df,term):
    """
    Exports data frame as Excel sheet
    :term: string term that was searched in the document will serve as title to the Excel sheet
    :param df: DataFrame of rows
    """
    
    file_path = f"./output/output_{term}.xlsx
    writer = pd.ExcelWriter(file_path, engine='xlsxwriter')
    df.to_excel(writer, term)
    writer.save()
    