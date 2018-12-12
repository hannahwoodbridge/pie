import sys, os
from unidecode import unidecode
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import config
from src.processing.preprocessing import preprocess
from src.searches.exact_search import find_exact_matches, count_exact_matches


def main_CROPS():
    file_name = config.CROPS['file_name']
    processed_df = preprocess(file_name)

    term = unidecode(sys.argv[1].lower())

    match_df = find_exact_matches(term, processed_df)
    print(count_exact_matches(term, match_df), match_df)


if __name__ == '__main__':
    main_CROPS()
