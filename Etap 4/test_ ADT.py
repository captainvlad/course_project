from ADT import StockADT
from arrays import Array

class TestADT():
    '''
    Class for testing ADT
    '''
    def __init__(self):
        '''
        obj -> None
        This method initializes an object
        '''
        self.setUP()
        self.test_fun()

    def setUP(self):
        '''
        obj -> None
        This method sets the objects to be tested
        '''
        self.example_1 = StockADT('TSLA')
        self.example_2 = StockADT('F')

    def test_fun(self):
        '''
        obj -> None
        This is method for testing
        '''
        assert(isinstance(self.example_1, StockADT))
        assert(isinstance(self.example_2, StockADT))

        assert(isinstance(self.example_1.array, Array))
        assert(isinstance(self.example_2.array, Array))

        assert(type(self.example_2.array.__getitem__(2)) == dict)
        assert(type(self.example_1.array.__getitem__(2)) == dict)

        assert(type(self.example_2.array.__getitem__(3)) == list)
        assert(type(self.example_1.array.__getitem__(3)) == list)

        assert(len(self.example_2.array.__getitem__(3)) == 5)
        assert(len(self.example_1.array.__getitem__(3)) == 5)

        assert(len(self.example_2.array.__getitem__(4)) == 2)
        assert(len(self.example_1.array.__getitem__(4)) == 2)

        assert(self.example_1.nname == 'TSLA')
        assert(self.example_2.nname == 'F')


a = TestADT()