import pandas as pd

class DataFormator:
    '''
    This class is used for data formation
    '''
    def __init__(self,name_of_file,name_of_second_file):
        '''
        object, str, str -> None
        This mehtod initializes an object
        '''
        self.name_of_file = name_of_file
        self.name_of_second_file = name_of_second_file
    def formator(self):
        '''
        object - > None
        This method takes 2 needed columns from csv file and writes them in a txt one.
        '''
        fil = open(self.name_of_file,'r')
        fil_2 = open(self.name_of_second_file,'w')

        df = pd.read_csv(fil)
        saved_column = df["Symbol"]
        saved_column_2 = df["Name"]
        i = 0
        while True:
            try:
                fil_2.write(saved_column[i])
                fil_2.write('    ')
                fil_2.write(saved_column_2[i])
                fil_2.write('\n')
                i += 1
            except:
                print('Done')
                fil.close()
                fil_2.close()
                break

fil = DataFormator('companylist.csv','company_trades_and_names.txt')
fil.formator()
