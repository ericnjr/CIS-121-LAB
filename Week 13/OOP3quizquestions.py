#Question 1
class Vector:
    def __init__(self, x, y):
        self.a = x
        self.b = y
    def __eq__(self, vector2):
        return self.a == vector2.a and self.b == vector2.b
    def __str__(self):
        return f"Vector: ({self.a}, {self.b})"

vector1 = Vector(3,4)
vector2 = Vector (3,8)
vector3 = Vector(2, 0)


#Question 2
import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self, point2):
        return self.x == point2.x and self.y == point2.y
    def distance(self, point2):
        return math.sqrt((self.x - point2.x)**2 + (self.y - point2.y)**2)
    def __str__(self):
        return f"Point: ({self.x}, {self.y})"
point1 = Point(3,4)
point2 = Point(0,0)
print(point1 == point2)
print(point1.distance(point2))
print(point1)



    


#Question 3
class LinearEquation:
    def __init__(self, m, b):
        self.m = m
        self.b = b
    def __add__(self, equation2):
        equation3 = LinearEquation(0, 0)
        equation3.m = self.m + equation2.m
        equation3.b = self.b + equation2.b
        return equation3
    def __str__(self):
        plus_or_minus_sign = None
        if self.b > 0:
            plus_or_minus_sign = "+"
        else:
            plus_or_minus_sign = ""
        print(plus_or_minus_sign)
        return f"Linear Equation: y = {self.m}x{plus_or_minus_sign}{self.b}"
y1 = LinearEquation(2, 3)
y2 = LinearEquation(-1, 5)
y3 = y1 + y2

print("Equation1 = ", y1)
print("Equation2 = ", y2)
print("Equation3 = ", y3)




#Question 4
class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes
    def __add__(self, time2):
        time3 = Time(0, 0)
        time3.hours = self.hours + time2.hours
        time3.minutes = self.minutes + time2.minutes
        if time3.minutes >= 60:
            time3.hours += time3.minutes // 60
            time3.minutes = time3.minutes % 60
        return time3
    def __str__(self):
        return f"Time: {self.hours} hours, {self.minutes} minutes"
time1 = Time(1, 30)
time2 = Time(2, 45)
time3 = time1 + time2

print("Time 1 = ", time1)
print("Time 2 = ", time2)
print("Time 3 = ", time3)


#Question 5
class RGBColor:
    #each parameter ranges from 0 -255
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
    def __add__(self, color2):
        color3 = RGBColor(0, 0, 0)
        color3.r = (self.r + color2.r) / 2
        color3.g = (self.g + color2.g) / 2
        color3.b = (self.b + color2.b) / 2
        return color3
    def __str__(self):
        return f"RGB Values: ({self.r}, {self.g}. {self.b})"
    
c1 = RGBColor(170, 150, 200)
c2 = RGBColor(30, 100, 60)
c3 = c1 + c2


print("Color1 = ", c1)
print("Color2 = ", c2)
print("Color3 = ", c3)

#Question 6
class RationalNumber:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        self.numerator = numerator
        self.denominator = denominator
    def __add__(self, r2):
        new_den = self.denominator * r2.denominator
        new_num = (self.numerator * r2.denominator) + (r2.numerator * self.denominator)
        return RationalNumber(new_num, new_den)
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

r1 = RationalNumber(1, 3)
r2 = RationalNumber(1, 2)

r3 = r1 + r2

print("r1 =", r1)
print("r2 =", r2)
print("r3 =", r3)

#Question 7
class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __eq__(self, cn2):
        return self.a == cn2.a and self.b == cn2.b
    def __str__(self):
        if self.b >=0:
            return f"{self.a} + {self.b}i"
        else:
            return f"{self.a}  {self.b}i"
    
z1 = ComplexNumber(3, 2)
z2 = ComplexNumber(-1, -4)
z3 = ComplexNumber(2, 0)
print(z1 == z2)
print(z1)
print(z2)
print(z3)

#Question 8
class Playlist:
    def __init__(self, name="New Playlist", songs= None):
        self.name = name
        if songs is None:
            self.songs = []
        else:
            self.songs = songs
    def add_song(self, song):
        self.songs.append(song)
    def __add__(self, other):
        combined = Playlist()
        combined.songs = self.songs + other.songs
        return combined
    def __str__(self):
        return f"{self.name}: {self.songs}"
    
pl1 = Playlist("My Playlist")
pl1.add_song("Song A")
pl1.add_song("Song B")
pl2 = Playlist("Other Playlist")
pl2.add_song("Song C")
pl3 = pl1 + pl2
print(pl3)







#Question 9  ###########
class ShoppingCart:
    def __init__(self, items = None):
        if items == None:
            self.items = {}
        else:
            self.items = items
    def add_item(self, item):
        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1
    def __add__(self, cart2):
        new_cart = ShoppingCart()
        for item, qty in self.items.items():
            new_cart.items[item] = qty
        for item, qty in cart2.items.items():
            if item in new_cart.items:
                new_cart.items[item] += qty
            else:
                new_cart.items[item] = qty
        return new_cart
    
    def __str__(self):
        return str(self.items)
    
p1 = ShoppingCart()
p1.add_item("tea")
p1.add_item("energy drink")
p1.add_item("energy drink")

p2 = ShoppingCart()
p2.add_item("energy drink")
p2.add_item("energy drink")
p2.add_item("energy drink")
p2.add_item("hat")

cart3 = p1 + p2

print("Cart 1:")
print(p1)
print("Cart 2:")
print(p2)
print("Combined Cart:")
print(cart3) 



    




#Question 10
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __mul__(self, n):
        # Multiply dimensions by n
        self.width *= n
        self.height *= n
        return self  # return the modified rectangle

    def __str__(self):
        return f"Rectangle({self.width} x {self.height})"


# Create a rectangle
r1 = Rectangle(4, 5)
print("Original:", r1)
print("Area:", r1.area())

# Multiply rectangle by an integer
r1 = r1 * 3

# Print the updated rectangle
print("After multiplying by 3:", r1)
print("New area:", r1.area())










