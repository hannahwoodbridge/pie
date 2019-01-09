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
    
    if len(sys.argv) > 2 :
        wantCase = sys.argv[2]=="-c"
        print('prise en compte casse')
    else:
        wantCase = False
        print('NON prise en compte casse')
    term = unidecode(sys.argv[1])
    match_df = find_exact_matches(term, df, wantCase)
    df_to_excel(match_df,term)

    print(f"Exact matches found: {count_exact_matches(term, match_df, wantCase)}")
    print("Output file is in folder ./output")



if __name__ == '__main__':
    main_CROPS()
