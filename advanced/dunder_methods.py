class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return self.name + ' ' + str(self.price)

    def __repr__(self):
        return f'<Product({self.name}, {self.price})>' #f-string用法

    def __add__(self, other):
        if isinstance(other, str):
            self.name += other
        if isinstance(other, Product):
            return [self, other]

    def __mul__(self, other):
        re = []
        if isinstance(other, int):
            for i in range(other):
                re.append(self)
        return re

    def print_name(self):
        print(self.name)


p1 = Product('珍珠奶茶', 60)
p2 = Product('義大利麵', 220)




class ShoppingCart:
    def __init__(self, products):
        self.products = products

    def __getitem__(self, key):
        return self.products[key]


s = ShoppingCart([p1, p2])

