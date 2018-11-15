import easygui as eg

def get_term():
    """
    A simple text entry box 
    """
    msg = "Enter a term to search in the database"
    title = "Exact Match Search"
    term = eg.enterbox(msg, title)

    return term
