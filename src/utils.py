import argparse


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'action',
        type=str,
        help="Action to perform: exact_search"
    )
    parser.add_argument(
        '--file_name',
        type=str,
        help="Source file, must end in .xlsx"
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

    return arguments
