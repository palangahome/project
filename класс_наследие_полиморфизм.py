class Building:
    year=None
    sity=None
    def __init__(self,year,sity):
        self.year=year
        self.sity=sity
        
    def info(self):
        print('Год ',self.year,'\nНазвание ',self.sity)


class Shop(Building):
    polka=0
    def __init__ (self, polka,year,city):
        super(Shop,self).__init__(year,city)
        self.polka=polka
    def info(self):
        super().info()
        print('Polka',self.polka)




shop=Shop(5,2000,'qqqq')
shop.info()