import sys, os
from unidecode import unidecode
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import config
from src.processing.preprocessing import preprocess
from src.searches.exact_search import find_exact_matches, count_exact_matches
from src.output.output import df_to_excel


def main_CROPS():
    file_name = config.CROPS['file_name']
    df = preprocess(file_name)

    term = unidecode(sys.argv[1].lower())
    match_df = find_exact_matches(term, df)
    df_to_excel(match_df,term)

    print(f"Exact matches found: {count_exact_matches(term, match_df)}")
    print("Output file is in folder ./output")



if __name__ == '__main__':
    main_CROPS()
