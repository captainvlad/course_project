from tkinter import *
from PIL import ImageTk, Image

class Represent:
    '''
    This is class for representation of made results
    '''
    def __init__(self):
        '''
        obj -> None
        This method initializes an object
        '''
        self.root = Tk()
        self.root.geometry("1200x500")

        T_2 = Text(self.root, height=1, width=60)
        T_2.pack(side=TOP)
        text_2 = "Первинний звіт та графік цін на акції обраної компанії:"
        T_2.insert(END, text_2)

        img = ImageTk.PhotoImage(Image.open("logo.png"))
        panel = Label(self.root, image=img)
        panel.pack(side = RIGHT)

        T = Text(self.root, height=8, width=40)
        T.pack(side=RIGHT)
        te = ""
        fil_1 = open("report.txt", "r", encoding='utf-8')
        for row in fil_1:
            te += row

        img_2 = ImageTk.PhotoImage(Image.open("chart.jpg"))
        panel_2 = Label(self.root, image=img_2)
        panel_2.pack(side = LEFT)

        T.insert(END, te)

        self.continu = False

        button = Button(self.root, text = "    Finish work!    ", bg = 'turquoise', fg = 'white', command = self.close)
        button.pack(side = BOTTOM)

        self.root.mainloop()

    def close(self):
        '''
        obj -> None
        This method closes the window
        '''
        self.root.destroy()
