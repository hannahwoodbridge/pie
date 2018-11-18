# PIE

To run, start by installing packages by entering into command line:

    pip install -r requirements.txt

Then run main.py with arguments the term to search for and the classifier to use:

    python src/main.py term model
    
This will run an exact search in ExempleCROPS.xlsx for the term entered. Returns the rows containing occurences of the term, and the total number of occurences. Then it will run a classifier on the entry categories (column category in the excel), returning a score.

The model to enter must belong to one of the options in config.py
