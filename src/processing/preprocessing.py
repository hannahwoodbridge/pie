from .utils import excel_to_df, remove_accents


def preprocess(file_name):
    """
    Does preprocessing of the file to search (accent removal)
    :param file_name:
    :return: preprocessed DataFrame
    """
    raw_df = excel_to_df(file_name)
    clean_df = remove_accents(raw_df, "COMMENTAIRE")

    return clean_df
