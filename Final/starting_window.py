from tkinter import *
from tkinter import *
from PIL import ImageTk, Image
from help_window import HelpWindow

class StartingWindow:
    '''
    This is class for creating starting windows
    '''


    def __init__(self):
        '''
        obj -> None
        This method initializes an object
        '''
        self.wrong = False
        self.root = Tk()
        self.root.geometry("800x600")

        button = Button(self.root, text = 'Info', bg = 'turquoise', fg = 'white', command = self.give_info)
        button.pack()

        labe = Label(text = 'Enter what company you want to discover: ')
        labe.pack()

        self.company = StringVar(self.root)
        self.name = ''
        com = Entry(self.root, textvariable = self.company)
        com.pack()

        button_1 = Button(self.root, text='             Start              ', bg='turquoise', fg='white', command=self.start)
        button_1.pack()

        button_2 = Button(self.root, text='Do not know which?', bg='turquoise', fg='white', command=self.give_file)
        button_2.pack()

        img = ImageTk.PhotoImage(Image.open("st.jpg"))
        panel = Label(self.root, image=img)
        panel.pack(side=TOP, fill="both", expand="yes")

        button_3 = Button(self.root, text='Quit', bg='turquoise', fg='white', command=self.quit)
        button_3.pack()

        self.root.mainloop()

    def give_info(self):
        '''
        obj -> None
        This method shows window with info
        '''
        a = HelpWindow(2) # just info

    def give_file(self):
        '''
        obj -> None
        This method shows window with info and companies
        '''
        a = HelpWindow(1) # companies

    def start(self):
        '''
        obj -> None
        This method checks wheather input by a user company exists
        '''
        self.name = self.company.get()
        Existance = False
        fil = open('company_trades_and_names.txt', 'r', encoding='utf-8')
        for row in fil:
            if self.name == row.split()[0] and len(self.name) > 0:
                Existance = True
                break
            else:
                pass

        if Existance == False:
            a = HelpWindow(3)

        else:
            self.root.destroy()

    def quit(self):
        '''
        obj -> None
        This method quits program
        '''
        self.root.destroy()
        self.company = 'quit'
