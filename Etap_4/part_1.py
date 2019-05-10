class User:
    '''
    This class gets information form user
    '''
    def __init__(self,info = None):
        '''
        object, str -> None
        This mehtod initializes an object
        '''
        self.info = info
        self.info_getter()

    def info_getter(self):
        '''
        objext -> None
        This method checks whether input company is in NASDAQ and helps if the user does not know what to do
        '''
        self.info = "1"
        Existance = False
        while self.info == "1":
            self.info = input("Enter what company's trademark you are interested in (if you do not know trademark, print 1):")
            if self.info != "1":
                fil = open('company_trades_and_names.txt', 'r')
                for row in fil:
                    if self.info in row:
                        Existance = True
                        break
                    else:
                        pass
                if Existance == False:
                    print("This company cannot be found on NASDQ")
                    self.info = "1"
            else:
                print('Here you can see following names of companies and their trademarks:')
                fil = open('company_trades_and_names.txt', 'r')
                for row in fil:
                    print(row)

        print(" Working on creating a chart ")
