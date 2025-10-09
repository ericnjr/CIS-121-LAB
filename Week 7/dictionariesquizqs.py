#Question 4
def get_names(names):
    result = []
    for key in names:
        result.append(names[key])  #key is tech id, value is name
    return result
print(get_names({"01475": "Steve", "87469": "Alice", "654123": "Bob"}))   
print(get_names({"ID1": "John", "ID2": "Emma", "ID3": "Liam"}))   
print(get_names({}))

#Question 5
def find_oldest(people):
    oldest_name = None
    oldest_age = -1
    for name, age in people.items():    #item/key is name, number is value
        if age > oldest_age:            
            oldest_age = age
            oldest_name = name
    return oldest_name
print(find_oldest({"Emma": 71, "Jack": 45, "Olivia": 82, "Liam": 39}))  
print(find_oldest({"Sophia": 50, "Mason": 68, "Ava": 67, "Noah": 33}))   
print(find_oldest({"Ethan": 25, "Lucas": 30, "Mia": 29})) 

#Question 6
def letter_count(word):
    counts = {}
    for letter in word:
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1
    return counts
print(letter_count("hello"))       
print(letter_count("mississippi")) 
print(letter_count("apple"))
#Question 7
def min_grade(exams):
    min_course = None
    min_score = float('inf') #starts with a very large number
    for course, grade in exams.items():
        if grade < min_score:
            min_score = grade
            min_course = course
    return min_course
print(min_grade({"Physics": 82, "Math": 65, "History": 75, "Biology": 95, "English": 87}))  
print(min_grade({"Chemistry": 78, "Algebra": 88, "History": 72, "Geography": 85}))          
print(min_grade({"Art": 90, "Music": 92, "Drama": 89})) 
#Question 8
def find_youngest(people):
    youngest_name = None
    youngest_age = float('inf')
    for name, age in people.items():
        if age < youngest_age:
            youngest_age = age
            youngest_name = name
    return youngest_name
print(find_youngest({"Emma": 71, "Jack": 45, "Olivia": 82, "Liam": 39}))  
print(find_youngest({"Sophia": 50, "Mason": 68, "Ava": 67, "Noah": 33}))    
print(find_youngest({"Ethan": 25, "Lucas": 30, "Mia": 29}))   

#Question 9
reciept = {}
reciept["Side Salad"] = 6
reciept["Chicken Parm"] = 12
reciept["Cookie"] = 3
total = sum(reciept.values())
print(total)


 #Question 10
menu = {}
menu["burger"] = 10
menu["fries"] = 4
menu["soda"] = 3
for item, price in menu.items():
    print(F"{item} cost {price}")
