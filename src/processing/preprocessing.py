from .utils import (excel_to_df,
                    remove_accents,
                    replace_acronyms_df)


def preprocess(file_name):
    """
    Does preprocessing of the file to search:
        Replace acronyms
        Remove accents
    :param file_name:
    :return: preprocessed DataFrame
    """
    df = excel_to_df(file_name, "data")
    # df = replace_acronyms_df(df, "comment")
    df = remove_accents(df, "comment")

    return df
