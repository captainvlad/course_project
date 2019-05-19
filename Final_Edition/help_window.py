from tkinter import *

class HelpWindow:
    '''
    This is class for creating help windows
    '''
    def __init__(self, config):
        '''
        obj, str -> None
        This method initializes an object
        '''
        self.root = Tk()
        self.root.geometry("350x200")

        message = ''

        if config == 1:
            fil = open('company_trades_and_names.txt', 'r', encoding='utf-8')
            for row in fil:
                message += row + '\n'

        elif config == 2:
            message = "This program is intended to make charts and brief short analysis on chosen companies and predictions.\n" \
                      "NOTE: user gets a chart with two lines where red one means top price each day while blue one means the lowest price\n" \
                      "© Vladyslav Zadorozhnyy"

        elif config == 3:
            message = "This company does not exist on NASDAQ"

        elif config == 4:
            message = "Wrong date is given or impossible to get all information"

        T = Text(self.root, height=10, width=40)
        T.pack()
        T.insert(END, message)

        button_2 = Button(self.root, text='OK', bg='turquoise', fg='white', command=self.close)
        button_2.pack()

        self.root.mainloop()

    def close(self):
        '''
        obj -> None
        This method destroys the window
        '''
        self.root.destroy()

