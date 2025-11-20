#Question 1
class Student:
    def __init__(self, name, major):
        self.name = name
        self.major = major
    def get_major(self):
        return self.major
    def set_major(self, major):
        self.major = major
    def __str__(self):
        return f"Student({self.name} is majoring in {self.major})"

class Course:
    def __init__(self, course_name, course_number):
        self.course_name = course_name
        self.course_number = course_number
        self.students = []
    def get_number(self):
        return self.course_number
    def set_number(self, course_number):
        self.course_number = course_number
    def add_student(self, student):
        self.students.append(student)
    def show_student_enrollment(self):
        print("Students Enrolled")
        for student in self.students:
            print(f"- {student}")
    def __str__(self):
        return F"Course(Name: {self.course_name}, Number: {self.course_number}, Enrolled: {len(self.students)} students)"
    
course1 = Course("Intro To Programming", 101)
student1 = Student("Eric", "MIS")
student2 = Student("Mike", "Finance")

course1.add_student(student1)
course1.add_student(student2)

print(course1)
course1.show_student_enrollment()


#Question 2
class Duck:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def get_color(self):
        return self.color
    def set_color(self, color):
        self.color = color
    def speak(self):
        print("Quack")

    def __str__(self):
        return f"Duck(Name: {self.name}, Color: {self.color})"
    
class Pond:
    def __init__(self, name):
        self.name = name
        self.ducks = []
    def add_duck(self, duck):
        self.ducks.append(duck)
    def ducks_quack(self):
        print(f"All ducks in {self.name} are quacking!")
        for duck in self.ducks:
            duck.speak()

    def __str__(self):
        return f"Pond(Name: {self.name}, Ducks: {len(self.ducks)} total)"

pond1 = Pond("Willow Pond")

duck1 = Duck("Mike", "White")
duck2 = Duck("Daisy", "Pink")

pond1.add_duck(duck1)
pond1.add_duck(duck2)

print(pond1)
pond1.ducks_quack()



#Question 3
class Lion:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def roar(self):
        print("Roar")
    def __str__(self):
        return f"Lion(Name: {self.name}, Gender: {self.gender})"
    
class Zoo:
    def __init__(self, location):
        self.location = location
        self.lions = []
    def add_lion(self, lion):
        self.lions.append(lion)
    def lions_roar(self):
        print(f"All lions in {self.location} are roaring!")
        for lion in self.lions:
            lion.roar()
    def count_lions(self):
        male_count = 0
        female_count = 0
        for lion in self.lions:
            if lion.gender == "male":
                male_count +=1
            else:
                female_count +=1
        print(f"{male_count} male, {female_count}, female")
    def __str__(self):
        return f"Zoo(Location: {self.location}, Lions: {len(self.lions)} total)"

zoo1 = Zoo("Madagascar Park")

lion1 = Lion("Simba", "male")
lion2 = Lion("Megan", "female")

zoo1.add_lion(lion1)
zoo1.add_lion(lion2)

print(zoo1)
zoo1.lions_roar()
zoo1.count_lions()



#Question 4
class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position
    def get_position(self):
        return self.position
    def set_posistion(self, position):
        self.position = position
    def __str__(self):
        return f"Employee(Name: {self.name}, Position: {self.position})"
    
class Department:
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget
        self.employees = []
    def get_budget(self):
        return self.budget
    def set_budget(self, budget):
        self.budget = budget
    def add_employee(self, employee):
        self.employees.append(employee)
    def show_staff_list(self):
        print("Staff List:")
        for employee in self.employees:
            print(f" -{employee}")
    def is_large(self):
        return len(self.employees) >= 10
    def __str__(self):
        return f"Department(Name: {self.name}, Budget: {self.budget}, Employees: {len(self.employees)})"

dept1 = Department("Human Resuources", 250000)

emp1= Employee("Mike", "HR Manager")
emp2= Employee("Luke", "Front Desk")

dept1.add_employee(emp1)
dept1.add_employee(emp2)

print(dept1)
dept1.show_staff_list()
print("Is the department large enough?", dept1.is_large())


#Question 5

class Droid:
    def __init__(self, designation, series):
        self.designation = designation
        self.series = series
    def get_designation(self):
        return self.designation
    def set_designation(self, designation):
        self.designation = designation
    def get_series(self):
        return self.series
    def set_series(self, series):
        self.series = series
    def communicate(self):
        print("Beep-Bloop-Blop")
    def __str__(self):
        return f"Robot(Designation: {self.designation}, Series: {self.series}"
    
class Starship:
    def __init__(self, name):
        self.name = name
        self.droids = []
    def add_droid(self, droid):
        self.droids.append(droid)
    def droids_communicate(self):
        for droid in self.droids:
            droid.communicate()
    def __str__(self):
        return f"Starship {self.name} with {len(self.droids)} droids"

ship1= Starship("Millenium Falcon")

droid1 = Droid("R2-D2", "cool")
droid2 = Droid("c-3PO", "lame")

ship1.add_droid(droid1)
ship1.add_droid(droid2)

print(ship1)
ship1.droids_communicate()


#Question 6
class Post:

    def __init__(self, caption, likes):
        self.caption = caption
        self.likes = likes
    def get_likes(self):
        return self.likes
    def add_like(self):
        self.likes += 1
    def display(self):
        print(f"Caption: {self.caption}")
    def __str__(self):
        return f"Post(Caption: {self.caption}, Likes: {self.likes})"

class Profile:
    def __init__(self, username):
        self.username = username
        self.posts = []
    def add_post(self, post):
        self.posts.append(post)
    def display_trending_posts(self):
        for post in self.posts:
            if post.get_likes() >= 10000:
                post.display()
            else:
                print("Not Trending")
    def __str__(self):
        return f"Profile: @{self.username} | {len(self.posts)} posts"
    
user_profile = Profile("Space Traveller")

post1 = Post("Exploring the rings of Saturn", 15000)
post2 = Post("Coffee on Mars", 8500)

    
user_profile.add_post(post1)
user_profile.add_post(post2)
print(user_profile)


user_profile.display_trending_posts()   
    
#Question 7
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def get_price(self):
        return self.price
    def set_price(self, price):
        self.price = price
    def display_details(self):
        print(f"Name: {self.name}, Price: {self.price}")
    def __str__(self):
        return f"Name: {self.name}, Price: {self.price}"
    
class ShoppingCart:
    def __init__(self, customer_id):
        self.customer_id = customer_id
        self.products = []
    def add_product(self, product):
        self.products.append(product)
    def calculate_total(self):
        total = 0
        for product in self.products:
            total += product.get_price()
        print(f"Total: {total}")   
        return total
    def __str__(self):
        return f"ShoppingCart for Customer #{self.customer_id} | {len(self.products)} products"   

cart = ShoppingCart(12345)

    
product1 = Product("Wireless Headphones", 79.99)
product2 = Product("Smart Watch", 149.50)

cart.add_product(product1)
cart.add_product(product2)

print(cart)

product1.display_details()
product2.display_details()

cart.calculate_total()





#Question 12
class TvShow:
    def __init__(self, title, genre):
        self.title = title
        self.genre = genre
    def get_genre(self):
        return self.genre
    def set_genre(self, genre):
        self.genre = genre
    def preview(self):
        print(f"Title: {self.title}, Genre: {self.genre}")
    def __str__(self):
        return f"Title: {self.title}, Genre: {self.genre}"
    
class NetflixDashboard:
    def __init__(self, profile_name):
        self.profile_name = profile_name
        self.shows = []
    def add_show(self, show):
        self.shows.append(show)
    def display_recommendations(self):
        for show in self.shows:
            print(F"Show Recommendations: {show}")
    def __str__(self):
        return f"Profile Name: {self.profile_name}, Shows: {len(self.shows)}"

dashboard1 = NetflixDashboard("Queezy")

show1 = TvShow("Friends", "Comedy")
show2 = TvShow("Scooby Doo", "Cartoon")

dashboard1.add_show(show1)
dashboard1.add_show(show2)

print(dashboard1)

dashboard1.display_recommendations()



    