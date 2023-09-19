class Book:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def getDetail(self):
        print('Name: %s' % self.name)
        print('Price: %d USD' % self.price)