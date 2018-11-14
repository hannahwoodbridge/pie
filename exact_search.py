import config
from interface import get_term
from preprocessing import excel_to_df


def count_exact_matches(term, df):
    """
    :param term: exact term to find in the data
    :param df: DataFrame to search in
    :return: total number of exact matches found
    """
    counted_df = df.COMMENTAIRE.str.count(term)
    return counted_df.sum()


def find_exact_term(term, df):
    """
    :param term: exact term to find in the data
    :param df: DataFrame to search in
    :return: DataFrame of rows where an exact match is found
    """

    return df[df.COMMENTAIRE.str.contains(term)]


file_name = config.CROPS['file_name']
data_df = excel_to_df(file_name)
term = get_term()
match_df = find_exact_term(term, data_df)
count_exact_matches(term, match_df)
