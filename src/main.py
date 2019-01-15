import sys, os
import argparse
from unidecode import unidecode
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import config
from src.processing.preprocessing import preprocess
from src.searches.exact_search import find_exact_matches, count_exact_matches
from src.output.output import write_output


def exact_search(term, case_sensitive):
    file_name_short = config.CROPS['file_name']
    file_name = f"{file_name_short}.xlsx"
    df = preprocess(file_name)

    match_df = find_exact_matches(term, df, case_sensitive)
    write_output(match_df, term, file_name_short)

    print(
        f"Exact matches found: "
        f"{count_exact_matches(term, match_df,case_sensitive)} \n"
        f"Output file is in folder ./output"
    )



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'action',
        type=str,
        help="Action to perform: exact_search"
    )
    parser.add_argument(
        '--term',
        type=str,
        help="The term to be searched"
    )
    parser.add_argument(
        '-cs',
        action='store_true',
        help="Imposes case sensitivity, otherwise it is ignored"
    )

    arguments = parser.parse_args()

    if arguments.action == 'exact_search':
        try:
            term = unidecode(arguments.term)
        except AttributeError:
            print("Missing term for exact search, please add --term='term'")
            quit()

        case_sensitive = arguments.cs
        exact_search(term, case_sensitive)
