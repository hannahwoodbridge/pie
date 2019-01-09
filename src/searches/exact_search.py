def count_exact_matches(term, df, wantCase = False):
    """
    :param term: exact term to find in the data
    :param df: DataFrame to search in
    :return: total number of exact matches found
    """
    if wantCase :
        counted_df = df.COMMENTAIRE.str.count(term)
    else :
        counted_df = df.COMMENTAIRE.str.count(term, flags = 2)
    return counted_df.sum()


def find_exact_matches(term, df, wantCase):
    """
    :param term: exact term to find in the data
    :param df: DataFrame to search in
    :return: DataFrame of rows where an exact match is found
    """

    return df[df.COMMENTAIRE.str.contains(term, case = wantCase)]
