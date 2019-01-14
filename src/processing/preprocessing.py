from .utils import (excel_to_df,
                    remove_accents,
                    remove_caps,
                    replace_acronyms_df)


def preprocess(file_name):
    """
    Does preprocessing of the file to search:
        Replace acronyms
        Remove caps
        Remove accents
    :param file_name:
    :return: preprocessed DataFrame
    """
    df = excel_to_df(file_name, "data")
    df = replace_acronyms_df(df, "COMMENTAIRE")
    #df = remove_caps(df, "COMMENTAIRE")
    df = remove_accents(df, "COMMENTAIRE")

    return df
