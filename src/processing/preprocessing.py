from .utils import excel_to_df, remove_accents, remove_caps


def preprocess(file_name):
    """
    Does preprocessing of the file to search (accent removal)
    :param file_name:
    :return: preprocessed DataFrame
    """
    raw_df = excel_to_df(file_name)
    lower_df = remove_caps(raw_df, "COMMENTAIRE")
    clean_df = remove_accents(lower_df, "COMMENTAIRE")

    return clean_df
