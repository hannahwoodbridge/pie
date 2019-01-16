# PIE

To run, start by installing packages by entering into command line:

    pip install -r requirements.txt

Then run main.py and display help to get argument information:

    cd src

    python main.py -h


EXACT SEARCH:

If action is specified to exact_search, a term is required (--term=TERM) and a case sensitivity flag is optional (-cs).

This will run an exact search in ExempleCROPS_1.xlsx for the term entered. Returns the rows containing occurrences of the term, and the total number of occurrences.

An working example you can search for is cougar.

CHOICE OF DATA SOURCE:

If you want to conduct a search on a data source other than ExempleCROPS_1.xlsx, add the file in .xlsx format to the data folder, then when running main.py add the argument --file_name=FILE_NAME

If the argument --file_name is not specified, the search is conducted by default on ExempleCROPS_1.xlsx
