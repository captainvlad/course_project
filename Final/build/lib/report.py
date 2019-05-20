from ADT import StockADT
from iexfinance.stocks import Stock

class General:
    '''
    This is main class for making a report on needed company
    '''
    def __init__(self, name):
        '''
        obj, str -> None
        This method initializes an object
        '''
        self.name = name
        self.array = StockADT(self.name)
        self.logo()
        self.rep()

    def logo(self):
        '''
        obj -> None
        This method saves logo of needed company
        '''
        from urllib.request import urlopen
        from PIL import Image, ImageTk

        imagefile = Image.open(urlopen(self.array.array.__getitem__(1)))
        imagefile.save('logo.png')

    def rep(self):
        '''
        obj, str -> None
        This method writes a report in a file
        '''
        fil = open('report.txt', 'w', encoding='utf-8')

        estimate = 0
        message = ''
        message += 'Коефіцієнт заборгованості: ' + str(self.array.array.__getitem__(3)[0])
        if self.array.array.__getitem__(3)[0] <= 0.3:
            message += ' (Прекрасний показник)\n'
            estimate += 2
        elif self.array.array.__getitem__(3)[0] <= 0.51:
            message += ' (Показник в нормі)\n'
            estimate += 1
        else:
            message += ' (Загрозливий показник)\n'

        message += 'Коефіцієнт покриття: ' + str(self.array.array.__getitem__(3)[1])
        if self.array.array.__getitem__(3)[1] > 1:
            message += ' (Показник в нормі)\n'
            estimate += 2
        else:
            message += ' (Загрозливий показник)\n'

        message += 'Коефіцієнт оборотності власного капіталу: ' + str(self.array.array.__getitem__(3)[2])
        if self.array.array.__getitem__(3)[2] >= 0.1:
            message += ' (Прекрасний показник)\n'
            estimate += 2
        elif self.array.array.__getitem__(3)[2] < 0:
            message += ' (Загрозливий показник)\n'
        else:
            message += ' (Показник в нормі)\n'
            estimate += 1

        message += 'Коефіцієнт рентабелбності власного капіталу: ' + str(self.array.array.__getitem__(3)[3])
        if self.array.array.__getitem__(3)[3] >= 0.1:
            message += ' (Прекрасний показник)\n'
            estimate += 2
        elif self.array.array.__getitem__(3)[2] < 0:
            message += ' (Загрозливий показник)\n'
        else:
            message += ' (Показник в нормі)\n'
            estimate += 1

        if self.array.array.__getitem__(3)[4] > 0:
            message += 'Чистий прибуток: '
            estimate += 1
        else:
            message += 'Чистий збиток: '
        message += str(self.array.array.__getitem__(3)[4]) + '\n'

        if (Stock(self.name).get_price()) > self.array.array.__getitem__(4)[1]:
            message += 'Ціна акцій компанії переживає свій пік і, згідно з стратегією черепах, зросте ще найближчим часом'
        elif (Stock(self.name).get_price()) < self.array.array.__getitem__(4)[0]:
            message += 'Ціна акцій компанії переживає кризу і, згідно з стратегією черепах, впаде ще найближчим часом'

        if estimate >= 10:
            message += '\n Компанія є надійною і показує вражаючі фінансові показники. Рейтинг: АА \n'
        elif estimate >= 8 and estimate < 10:
            message += '\n Компанія є надійною і показує вражаючі фінансові показники. Рейтинг: А \n'
        elif estimate >= 6 and estimate < 8:
            message += '\n Компанія є стійкою і показує стабільні фінансові показники. Рейтинг: BB \n'
        elif estimate >= 5:
            message += 'Компанія є нестійкою і показує признаки можливого фінансового погіршення в майбутньому. Рейтинг: B \n'
        else:
            message += 'Компанія близька до серйозного фінансового краху.Інвестування в компанію не рекомендується  Рейтинг: C \n'


        fil.write(message)
        fil.close()