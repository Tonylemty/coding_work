from dunder_methods import Product #parent class

#child class
class Drink(Product):
    #override 取代
    def __init__(self, name, price, volume):
        super().__init__(name, price) #呼叫原程式
        self.volume = volume
    

d = Drink('珍珠奶茶', 80, 600)
print(d.name)
print(d.volume)



'''
class Food(Product): #等同於以下幾行
    pass

Food = type('Food', (Product, ), {})
f = Food('義大利麵', 220)
print(type(f))
'''