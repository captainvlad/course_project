from starting_window import StartingWindow
from time_window import TimeWindow
from graph_creator import GraphCreator
from help_window import HelpWindow
from report import General
from represent_results import Represent

class Start:
    '''
    This is class to start and rule the program
    '''
    def __init__(self):
        '''
        obj -> None
        This method initializes an object
        '''
        self.conti = True
        self.wrong = False
        self.element_1 = StartingWindow()
        if self.element_1.name != 'quit' and len(self.element_1.name) > 0:
            self.element_2 = TimeWindow()
            self.get_chart()
            self.get_rep()
            if self.element_2 != None:
                a = Represent()



    def get_chart(self):
        '''
        obj -> None
        This makes a graphic chart
        '''
        try:
            GraphCreator(self.element_1.name, int(self.element_2.year), int(self.element_2.month), int(self.element_2.day))
        except:
            self.element_2 = None
            HelpWindow(4)

    def get_rep(self):
        '''
        obj, str -> None
        This method makes a report
        '''
        try:
            General(self.element_1.name)
        except:
            HelpWindow(4)
            self.wrong = True


a = Start()