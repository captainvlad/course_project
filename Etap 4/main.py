from part_1 import User
from ADT import StockADT
from graph_creator import GraphCreator
from tkinter import *
from iexfinance.stocks import Stock

class General:
    def __init__(self):
        a = User()
        self.array = StockADT(a.info)
        self.name = a.info
        GraphCreator(a.info)
        print(self)
        #self.logo()
        self.eternal_price()

    def logo(self):
        from urllib.request import urlopen
        from PIL import Image, ImageTk

        imagefile = Image.open(urlopen(self.array.array.__getitem__(1)))
        imagefile.save('logo.png')

        app_root = Tk()

        # Setting it up
        img = ImageTk.PhotoImage(Image.open("logo.png"))

        # Displaying it
        imglabel = Label(app_root, image=img).grid(row=1, column=1)

        app_root.mainloop()

    def __str__(self):
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


        return message

    def eternal_price(self):
        import time
        import datetime
        import pytz
        now = datetime.datetime.now(tz=pytz.timezone('US/Eastern'))
        print('Current price')
        if now.hour > 9 and now.weekday() < 5:
            while True:
                print(Stock(self.name).get_price())
                time.sleep(5)
        else:
            print(Stock(self.name).get_price())
            print('NASDAQ working hours: 9:30 a.m to 4 p.m. in New York. From Monday to Friday. It\'s closed right know.' )



General()