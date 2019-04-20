from part_1 import User
from ADT import StockADT

class General:
    def __init__(self):
        a = User()
        b = StockADT(a.info)

        for i in range(1,5):
            print(b.array.__getitem__(i))

example_1 = General()

# from urllib.request import urlopen
# from PIL import Image
#
# img = Image.open(urlopen(b.logo))
# img.show()