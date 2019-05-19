from tkinter import *

class TimeWindow:
    '''
    This is class for creating window to now time for chart
    '''
    def __init__(self):
        '''
        obj -> None
        This method initializes an object
        '''
        self.root = Tk()
        self.root.geometry("400x150")

        labe = Label(text='Enter what year you want to get chart from (later than 1975): ')
        labe.pack()

        self.year = StringVar(self.root)
        com = Entry(self.root, textvariable=self.year)
        com.pack()

        labe = Label(text='Enter what month you want to get chart from (positive integer): ')
        labe.pack()

        self.month = StringVar(self.root)
        com = Entry(self.root, textvariable=self.month)
        com.pack()

        labe = Label(text='Enter what day you want to get chart from (positive integer): ')
        labe.pack()

        self.day = StringVar(self.root)
        com = Entry(self.root, textvariable=self.day)
        com.pack()

        button = Button(self.root, text='OK', bg='turquoise', fg='white', command=self.finish_timing)
        button.pack()

        self.root.mainloop()

    def finish_timing(self):
        '''
        obj -> None
        This is method takes what the user's input
        '''
        self.year = self.year.get()
        self.month = self.month.get()
        self.day = self.day.get()
        self.root.destroy()