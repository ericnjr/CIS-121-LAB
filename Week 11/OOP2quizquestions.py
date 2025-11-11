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




