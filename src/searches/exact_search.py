import re
import pandas as pd


def count_exact_matches(term, results, case_sensitive=False):
    """
    :param term: exact term to find in the data
    :param results: DataFrame to search in
    :return: total number of exact matches found
    """
    if results.empty:
        return 0
    else:
        matches = results['matches'].apply(
            pd.Series
        ).stack().reset_index(drop=True)

        if case_sensitive:
            return sum(matches.str.count(term))
        else:
            return sum(matches.str.count(term, flags=2))


def find_exact_matches(term, df, case_sensitive=False):
    """
    :param term: exact term to find in the data
    :param df: DataFrame to search in
    :return: DataFrame of rows where an exact match is found
    """
    results = df[
        df.comment.str.contains(term,
                                    case=case_sensitive)
    ].reset_index()

    if not results.empty:
        if case_sensitive:
            results['matches'] = results.apply(
                lambda x: re.findall(term, x['comment']), axis=1)
        else:
            results['matches'] = results.apply(
                lambda x: re.findall(term,
                                     x['comment'],
                                     flags=re.I),
                axis=1)

    return results
