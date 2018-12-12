import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import config
from src.processing.preprocessing import excel_to_df
from src.searches.exact_search import find_exact_matches, count_exact_matches
from src.output.output import df_to_excel
# from src.searches.classification import classify


def main():
    file_name = config.CROPS['file_name']
    data_df = excel_to_df(file_name)
    term = sys.argv[1]
    match_df = find_exact_matches(term, data_df)
    df_to_excel(match_df,term)
    print(f"exact matches found: {count_exact_matches(term, match_df)}")
    print("Le fichier output est à l'adresse ./output")


if __name__ == '__main__':
    main()
