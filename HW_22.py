class Item:
    def __init__(self, name, price, description, dimensions):
        self.name = name
        self.price = price
        self.description = description
        self.dimensions = dimensions

    def __str__(self):
        return f"Item[name = {self.name}, price = {self.price}, description = {self.description}, dimension = {self.dimensions}]"

class User:

    def __init__(self, name, surname, phonenumber):
        self.name = name
        self.surname = surname
        self.phonenumber = phonenumber

    def __str__(self):
        return f"User[name = {self.name}, surname = {self.surname}, phonenumber = {self.phonenumber}]"

class Purchase():
    def __init__(self, user):
        self.products = {}
        self.user = user
        self.total = 0

    def add_to_cart(self, product, value):
        self.products[product] = value
        return value

    def get_total_value(self):
        self.total = sum(self.products.values())
        return self.total

    def __str__(self):
        items_str = "\n".join([f"{product}: {count}" for product, count in self.products.items()])
        for product, count in self.products.items():
            items_str += f'{str(product)}:{count}'
        return f"Purchase by {self.user}:\n{items_str}\nTotal: {self.get_total_value()}"


item_1 = Item("box", "10$", "big", "20x30")
item_2 = Item("table", "80$", "office table", "60x100")
print(item_1)
print(item_2)

user_1 = User("Ivan", "Petrov", "0504223452")
user_2 = User("Taras", "Sobko", "0662635423")
print(user_1)
print(user_2)

cart = Purchase(user_1)
cart.add_to_cart(item_1, 4)
cart.add_to_cart(item_2, 2)
print(cart)




