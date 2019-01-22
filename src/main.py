import sys, os
from unidecode import unidecode
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import config
from src.searches.exact_search import exact_search
from src.utils import get_arguments


if __name__ == '__main__':
    arguments = get_arguments()

    file_name = arguments.file_name
    if not file_name:
        file_name = config.DEFAULT['file_name']
        print(
            f"No file specified, using default file "
            f"{config.DEFAULT['file_name']}"
        )

    if arguments.action == 'exact_search':
        try:
            term = unidecode(arguments.term)
        except AttributeError:
            print("Missing term for exact search, please add --term=TERM")
            quit()

        case_sensitive = arguments.cs
        exact_search(file_name, term, case_sensitive)
