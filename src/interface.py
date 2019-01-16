import tkinter as tk 
import tkcalendar
from tkinter import simpledialog
from PIL import Image, ImageTk

class MainWindow(tk.Frame):
    """Displays the data interface in a more good-looking way"""
    def __init__(self, master, root, OPTIONS):
        #Image frame
        self.frame1 = tk.Frame(master)
        self.frame1.grid(row=1, column=1)
        self.image = ImageFrame(self.frame1)
        
        #Data frame
        self.frame2 = tk.Frame(master)
        self.frame2.grid(row=1, column=2)
        self.window = DataWindow(self.frame2, root,OPTIONS)
        
        master.grid()
        

class DataWindow(tk.Frame):
    """Interface to select all the inputs"""
    def __init__(self, master, root, OPTIONS):
        self.root=root
        self.master=master
        self.label = tk.Label(master, 
                              text="Enter a term to search in the database")
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
        
        #Creation of selection dates  
        self.date1=""
        self.date2=""
        button = tk.Button(master, text="Selectionnez la premiere date", 
                           command=self.onclick_date1)
        button.pack()
               
        button = tk.Button(master, text="Selectionnez la seconde date", 
                           command=self.onclick_date2)
        button.pack()
        
        #Validation or cancelation buttons
        frame = tk.Frame(master)
        frame.pack()
        self.OK = tk.Button(frame, text="OK", command=self.get_search)
        self.OK.pack(side=tk.LEFT)
        self.cancel=tk.Button(frame, text="Cancel", command=root.destroy)
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
        self.root.destroy()
        
    def onclick_date1 (self):
        """
        Class method to update the date selected in the calendar box
        """
        cd = CalendarDialog(self.master)
        self.date1=cd.result
        
    def onclick_date2 (self):
        """
        Class method to update the date selected in the calendar box
        """
        cd = CalendarDialog(self.master)
        self.date2=cd.result
        

class CalendarDialog(simpledialog.Dialog):
    """Dialog box that displays a calendar and returns the selected date"""
    def body(self, master):
        self.calendar = tkcalendar.Calendar(master)
        self.calendar.pack()

    def apply(self):
        self.result = self.calendar.get_date()      
   


class ImageFrame(tk.Frame):
    """Frame displaying the Logo de l'Armée de Terre"""
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.original = Image.open('./data/logo_ADT.png')
        resized = self.original.resize((600, 468), Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(resized) # Keep a reference, prevent GC
        imagelabel = tk.Label(self, image = self.image)
        imagelabel.grid(row=1,column=1)
        self.grid()
        

def get_search_data():
    """
    A simple text and search parameters entry box
    OPTIONS list needs to be updated when a new type of search is implemented
    
    """
    #List of search options
    OPTIONS = [
        "exact_search",
        "exact_search case_sensitivity",
        "synonyms_search"
    ]
    
    # Creation of window interface
    root = tk.Tk()
    root.title("Search")
    I = MainWindow(root,root,OPTIONS)
    root.mainloop()
    
    return I.window.term, I.window.search_type, I.window.date1, I.window.date2

########## Displaying results #########
       
class DispWindow(tk.Frame):
    """
    Class defining the window object that displays the result of the search
    """
    def __init__(self, master):
        self.master=master
        
        #Displaying number of events found
        frame1=tk.Frame(master)
        frame1.pack()
        self.var_nb_event=tk.StringVar()
        self.var_nb_event.set("")
        self.text_event=tk.Label(frame1, text="Number of events found:")
        self.event=tk.Label(frame1, textvariable=self.var_nb_event)
        self.text_event.pack(side=tk.LEFT)
        self.event.pack(side=tk.RIGHT)
        
        #Displaying time for calculation
        frame2=tk.Frame(master)
        frame2.pack()
        self.var_time=tk.StringVar()
        self.var_time.set("")
        self.text_time=tk.Label(frame2, text="Time for calculation:")
        self.time=tk.Label(frame2, textvariable=self.var_time)
        self.text_time.pack(side=tk.LEFT)
        self.time.pack(side=tk.RIGHT)
        
        #Validation button
        self.OK = tk.Button(master, text="OK", command=master.destroy)
        self.OK.pack()

    def update(self,nb_events, time):
        """
        A class method to update the labels in the window
        :param nb_events: number of events found
        :param time: time of calculation
        """
        self.var_nb_event.set(str(nb_events))
        self.var_time.set(str(time))
        #self.master.update_idletasks()

def disp_search_result(nb_events, time, term, search_type):
    """
    A box that displays the number of events and time of calculation
    
    """
    
    root=tk.Tk()
    root.title(f"Searching {term} with option {search_type}")
    window = DispWindow(root)
    window.update(nb_events,time)
    root.mainloop()