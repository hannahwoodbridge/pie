import easygui as eg

def get_term():
    msg = "Enter a term to search in the database"
    title = "Exact Match Search"
    term = eg.enterbox(msg, title)

    return term
