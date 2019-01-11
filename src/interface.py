import tkinter as tk 

class MainWindow(tk.Frame):
    def __init__(self, master, OPTIONS):
        self.master=master
        self.label = tk.Label(master, text="Enter a term to search in the database")
        self.label.pack()
        
        #Setting term and search parameters initial values
        self.term=""
        self.search_type=tk.StringVar(master)
        self.search_type.set("Select type of search")
        
        #Creation of term entry line
        self.term_line = tk.Entry(master, textvariable=str, width=30)
        self.term_line.pack()
        
        #Creation of search options menu
        args = (master, self.search_type) + tuple(OPTIONS)
        self.search_list = tk.OptionMenu(*args)
        self.search_list.pack()
        
        #Validation or cancelation buttons
        frame = tk.Frame(master)
        frame.pack()
        self.OK = tk.Button(frame, text="OK", command=self.get_search)
        self.OK.pack(side=tk.LEFT)
        self.cancel=tk.Button(frame, text="Cancel", command=master.destroy)
        self.cancel.pack(side=tk.RIGHT)
        
        
        
    def get_search(self):
        """
        Class method to update term and search_type values with the data 
        entered in the interface
        """
        self.term = self.term_line.get()
        self.search_type =  self.search_type.get()
        if self.term=="":
            raise ValueError('Please enter a term to be searched in database')
        if self.search_type=="Select type of search":
            raise ValueError('Please select a type of search')
        self.master.destroy()
        
        
        
   

def get_search_data():
    """
    A simple text and search parameters entry box
    OPTIONS list needs to be updated when a new type of search is implemented
    
    """
    #List of search options
    OPTIONS = [
        "Exact_search",
        "CASSE_search",
        "Search_by_family"
    ]
    
    # Creation of window interface
    root = tk.Tk()
    root.title("Search")
    window = MainWindow(root,OPTIONS)
    root.mainloop()
    
    return window.term, window.search_type

