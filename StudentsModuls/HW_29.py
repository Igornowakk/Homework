class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def __eq__(self, other):
        return self.get_square() == other.get_square()

    def __add__(self, other):
        add_width = self.width + other.width
        add_height = self.height + other.height
        return Rectangle(add_width, add_height)

    def __mul__(self, n):
        mul_width = self.width * n
        mul_height = self.height * n
        return Rectangle(mul_width, mul_height)

    def __sub__(self, other):
        sub_width = self.width - other.width
        sub_height = self.height - other.height
        return Rectangle(sub_width, sub_height)

    def __str__(self):
        return f"Rectangle: width={self.width}, height={self.height}"


r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
assert r1.get_square() == 8
assert r2.get_square() == 18

r3 = r1 + r2
assert r3.get_square() == 50

r4 = r1 * 4
assert r4.get_square() == 128

r5 = r3 - r1
assert r5.get_square() == 18

print(r3)
print(r4)
print(r5)
print(r1.get_square())
print(r2.get_square())
print(r3.get_square())
print(r4.get_square())
print(r5.get_square())
print(r1.__eq__(r2))
print(r2.__eq__(r5))
