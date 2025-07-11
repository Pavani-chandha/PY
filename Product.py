class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def getName(self):
        print(self.name)
    def getPrice(self):
        print(self.price)
s1=Product(name = "soap", price = 50)
s2=Product(name="shampoo",price=20)
s1.getName()
s1.getPrice()
s2.getName()
s2.getPrice()
print(s2.name)
print(s2.price)