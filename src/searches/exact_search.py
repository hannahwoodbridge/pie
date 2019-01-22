import re
import pandas as pd
import config
from ..processing.preprocessing import preprocess
from ..output.output import write_output


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
        df.comment.str.contains(term, case=case_sensitive)
    ].reset_index(drop=True)

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


def exact_search(file_name, term, case_sensitive):
    """
    Runs an exact search of a term in a file, writes to output
    and counts matches
    :param file_name: file to search
    :param term: term to search
    :param case_sensitive: True if search is to be case sensitive
    :return: None
    """
    df = preprocess(file_name)
    match_df = find_exact_matches(term, df, case_sensitive)
    write_output(match_df, term, file_name)

    print(
        f"Exact matches found: "
        f"{count_exact_matches(term, match_df, case_sensitive)} \n"
        f"Output file is in folder ./output"
    )
