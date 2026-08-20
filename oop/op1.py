class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    # + operator
    def __add__(self, other):
        return self.price + other.price

    # > operator
    def __gt__(self, other):
        return self.price > other.price

    # == operator
    def __eq__(self, other):
        return self.price == other.price


p1 = Product("Laptop", 80000)
p2 = Product("Phone", 30000)

print(p1 + p2)
print(p1 > p2)
print(p1 == p2)