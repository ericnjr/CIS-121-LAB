
#Question 1
class Product:
    def __init__(self, _name, _price, _quantity):
        self.name = _name
        self.price = _price
        self.quantity = _quantity
    def get_name(self):
        return self.name
    def set_name(self, _name):
        self.name = _name 
    def get_price(self):
        return self.price
    def set_price(self, _price):
        self.price = _price
    def get_quantity(self):
        return self.quantity
    def set_quantity(self, _quantity):
        self.quantity = _quantity
product1 = Product("Laptop", 999.99, 10)

print(product1.get_name())      # Laptop
print(product1.get_price())     # 999.99
print(product1.get_quantity())  # 10



#Question 2
class Book:
    def __init__(self, _title, _author, _page_count):
        self.title = _title
        self.author = _author
        self.page_count = _page_count
    def get_title(self):
        return self.title
    def set_title(self, _title):
        self.title = _title
    def get_author(self):
        return self.author
    def set_author(self, _author):
        self.author = _author
    def get_page_count(self):
        return self.page_count
    def set_page_count(self, _page_count):
        self.page_count = _page_count


book1 = Book("To Kill a Mockingbird", "Harper Lee", 281)

# Displaying the book details
print("Title:", book1.get_title())
print("Author:", book1.get_author())
print("Page Count:", book1.get_page_count())






#Question 3
class Movie:
    def __init__(self, _title, _director, _runtime_minutes):
        self.title = _title
        self.director = _director
        self.runtime_minutes = _runtime_minutes
    def get_title(self):
        return self.title
    def set_title(self, _title):
        self.title = _title
    def get_director(self):
        return self.director
    def set_director(self, _director):
        self.director = _director
    def get_runtime_minutes(self):
        return self.runtime_minutes
    def set_runtime_minutes(self, _runtime_minutes):
        self.runtime_minutes = _runtime_minutes

movie1 = Movie("Goonies", "Michael Jordan", 120)

print("Title:", movie1.get_title())
print("Director:", movie1.get_director())
print("Runtime Minutes:", movie1.get_runtime_minutes())

#Question 4
class Song:
    def __init__(self, _title, _artist, _duration_seconds):
        self.title = _title
        self.artist = _artist
        self.duration_seconds = _duration_seconds
    def get_title(self):
        return self.title
    def set_title(self, _title):
        self.title = _title
    def get_artist(self):
        return self.artist
    def set_artist(self, _artist):
        self.artist = _artist
    def get_duration_seconds(self):
        return self.duration_seconds
    def set_duration_seconds(self, _duration_seconds):
        self.duration_seconds = _duration_seconds

song1 = Song("Chattahhoche", "Alan Jackson", 180)

print("Title:", song1.get_title())
print("Artist:", song1.get_artist())
print("Duration Seconds:", song1.get_duration_seconds())

#Question 5
class Employee:
    def __init__(self, _name, _title, _salary):
        self.name = _name
        self.title = _title
        self.salary = _salary
    def get_name(self):
        return self.name
    def set_name(self, _name):
        self.name = _name
    def get_title(self):
        return self.title
    def set_title(self, _title):
        self.title = _title
    def get_salary(self):
        return self.salary
    def set_salary(self, _salary):
        self.salary = _salary
    def greeting(self):
        print(f"Hello. My name is {self.name}. I'm the {self.title}")    
    def raise_request(self):
        new_salary = self.salary * 1.06
        print(f"I'm currently making {self.salary}. I'd like to make a new salary of {new_salary}")
employee1 = Employee("Eugene", "CEO", 100.00)

# Calling the methods
employee1.greeting()
employee1.raise_request()

#Question 6
class Student:
    def __init__(self, _name, _major, _GPA):
        self.name = _name
        self.major = _major
        self.GPA = _GPA
    def get_name(self):
        return self.name
    def set_name(self, _name):
        self.name = _name
    def get_major(self):
        return self.major
    def set_major(self, _major):
        self.major = _major
    def get_GPA(self):
        return self.GPA
    def set_GPA(self, _GPA):
        self.GPA = _GPA
    def introduction(self):
        print(f"Hi, I'm {self.name}. I'm studying {self.major}")
    def grade_point(self):
        new_gpa = self.GPA + .2
        print(f"I'm hitting the books! My GPA increased from {self.GPA} to {new_gpa}.")

student1 = Student("Michael", "MIS", 3.5)

student1.introduction()
student1.grade_point()

#Question 7
class Vehicle:
    def __init__(self, _make, _model, _year):
        self.make = _make
        self.model = _model
        self.year = _year
    def get_make(self):
        return self.make
    def set_make(self, _make):
        self.make = _make
    def get_model(self):
        return self.model
    def set_model(self, _model):
        self.model = _model
    def get_year(self):
        return self.year
    def set_year(self, _year):
        self.year = _year
    def print_vehicle_type(self):
        print(f"{self.year} {self.make} {self.model}")

vehicle1 = Vehicle("GMC", "Sierra", 2005)

vehicle1.print_vehicle_type()

#Question 8
class Course:
    def __init__(self, _course_code, _course_name, _instructor):
        self.course_code = _course_code
        self.course_name = _course_name
        self.instructor = _instructor
    def get_course_code(self):
        return self.course_code
    def set_course_code(self, _course_code):
        self.course_code = _course_code
    def get_course_name(self):
        return self.course_name
    def set_course_name(self, _course_name):
        self.course_name = _course_name
    def get_instructor(self):
        return self.instructor
    def set_instructor(self, _instructor):
        self.instructor = _instructor
    def print_info(self):
        print(f"{self.course_code}: {self.course_name} taught by {self.instructor}")

course1 = Course("CIS101", "Introduction to Programming", "Matt Priem")

course1.print_info()

#Question 9
class Point:
    def __init__(self, _x_coor, _y_coor):
        self.x_coor = _x_coor
        self.y_coor = _y_coor
    def get_x_coor(self):
        return self.x_coor
    def set_x_coor(self, _x_coor):
        self.x_coor = _x_coor
    def get_y_coor(self):
        return self.y_coor
    def set_y_coor(self, _y_coor):
        self.y_coor = _y_coor
    def print_info(self):
        print(f"(x,y) = ({self.x_coor},{self.y_coor})")

point1 = Point(4, 5)

point1.print_info()

#Question 10
import math
class Vector:
    def __init__(self, _x_dir, _y_dir):
        self.x_dir = _x_dir
        self.y_dir = _y_dir
    def get_x_coor(self):
        return self.x_dir
    def set_x_coor(self, _x_dir):
        self.x_dir = _x_dir
    def get_y_coor(self):
        return self.y_dir
    def set_y_coor(self, _y_dir):
        self.y_dir = _y_dir
    def get_magnitude(self):
        magnitude = math.sqrt(self.x_dir **2 + self.y_dir **2)
        print(magnitude)

vector1 = Vector(5, 9)

vector1.get_magnitude()

#Question 11
class ColorRGB:
    def __init__(self, _red, _green, _blue):
        self.red = _red
        self.green = _green
        self.blue = _blue
    def get_red(self):
        return self.red
    def set_red(self, _red):
        self.red = _red
    def get_green(self):
        return self.green
    def set_green(self, _green):
        self.green = _green
    def get_blue(self):
        return self.blue
    def set_blue(self, _blue):
        self.blue = _blue
    def to_grayscale(self):
        value = 0.3 * self.red + 0.59 * self.green + 0.11 * self.blue
        print(value)
colorrgb1 = ColorRGB(120, 100, 150)
colorrgb1.to_grayscale()

#Question 12
class TemperatureInCelsius:
    def __init__(self, _temp_value):
        self.temp_value = _temp_value
    def get_temp_value(self):
        return self.temp_value
    def set_temp_value(self, _temp_value):
        self.temp_value = _temp_value
    def to_fahrenheit(self):
        fahrenheit = ((self.temp_value * 9/5) + 32)
        print(fahrenheit)
temp1 = TemperatureInCelsius(30)
temp1.to_fahrenheit()

#Question 13
class Rectangle:
    def __init__(self, _width, _height):
        self.width = _width
        self.height = _height
    def get_width(self):
        return self.width
    def set_width(self, _width):
        self.width = _width
    def get_height(self):
        return self.height
    def set_height(self, _height):
        self.height = _height
    def calculate_area(self):
        area = self.width * self.height
        print(area)
rectangle1 = Rectangle(5, 10)
rectangle1.calculate_area()

#Question 14
import math
class Circle:
    def __init__(self, _radius):
        self.radius = _radius
    def get_radius(self):
        return self.radius
    def set_radius(self, _radius):
        self.radius = _radius
    def calculate_circumference(self):
        circumference = 2 * math.pi * self.radius
        print(circumference)
circle1 = Circle(5)
circle1.calculate_circumference()

#Question 15
class Recipe:
    def __init__(self, _name, _cooking_time):
        self.name = _name
        self.cooking_time = _cooking_time
    def get_name(self):
        return self.name
    def set_name(self, _name):
        self.name = _name
    def get_cooking_time(self):
        return self.cooking_time
    def set_cooking_time(self, _cooking_time):
        self.cooking_time = _cooking_time
    def is_quick_meal(self):
        return self.cooking_time < 30
    
recipe1 = Recipe("Fish", 10)
print(recipe1.is_quick_meal())  

recipe2 = Recipe("Lasagna", 45)
print(recipe2.is_quick_meal())      



