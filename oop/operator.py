class Product:

    def __init__(self, price):
        self.price = price

    def __eq__(self, other):
        return self.price == other.price

    def __ne__(self, other):
        return self.price != other.price

    def __gt__(self, other):
        return self.price > other.price

    def __lt__(self, other):
        return self.price < other.price

    def __ge__(self, other):
        return self.price >= other.price

    def __le__(self, other):
        return self.price <= other.price


p1 = Product(100)
p2 = Product(200)

print(p1 == p2)
print(p1 != p2)
print(p1 > p2)
print(p1 < p2)
print(p1 >= p2)
print(p1 <= p2)