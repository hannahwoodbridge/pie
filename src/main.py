import sys, os
import argparse
from unidecode import unidecode
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import config
from src.processing.preprocessing import preprocess
from src.searches.exact_search import find_exact_matches, count_exact_matches
from src.interface import get_search_data, disp_search_result
from src.output.output import write_output
import time


def exact_search(term, case_sensitive=False):
    file_name_short = config.CROPS['file_name']
    file_name = f"{file_name_short}.xlsx"
    start=time.time()                       
    df = preprocess(file_name)
    match_df = find_exact_matches(term, df, case_sensitive)
    write_output(match_df, term, file_name_short)
    end = time.time()

    diff_time = end - start
    disp_search_result(count_exact_matches(term, match_df,case_sensitive), 
                       diff_time, term, search_type)

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
    
    ##### Use of interface instead of passing arguments #######
    if  arguments.action == 'interface':
        term,search_type,date_1,date_2 = get_search_data()
        if search_type=="exact_search":
            exact_search(term)
        elif search_type=="exact_search case_sensitivity":
            case_sensitive = True
            exact_search(term, case_sensitive)
        else:
            print(f"{search_type} not implemented yet")
            quit()
            
