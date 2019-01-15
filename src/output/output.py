import pandas as pd

def write_output(results, term, input_file):
    """
    Exports data frame results as Excel sheet
    :param results: DataFrame of rows to return
    :param term: string term that was searched in the document
    :param input_file: file being searched
    :return: Excel sheet of the matched rows
    """

    file_path = f"./output/output_{term}_{input_file}.xlsx"
    writer = pd.ExcelWriter(file_path, engine='xlsxwriter')
    results.to_excel(writer, term)
    writer.save()
