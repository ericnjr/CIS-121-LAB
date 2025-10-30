#Question 1  #isogram is a word where no letter is repeated
def is_isogram(word):
    return len(word) == len(set(word))#set removes duplicates
print(is_isogram("algorithm"))
print(is_isogram("password"))






#Question 2
def find_unique(numbers):
    for num in numbers:
        if numbers.count(num) == 1:
            return num
print(find_unique([1, 2, 2, 3, 3, 4, 4]))          
print(find_unique([7, 8, 8, 9, 9, 10, 10]))       
print(find_unique([5, 6, 6, 7, 7, 8, 8, 5, 9]))







#Question 3
def return_unique(numbers):
    unique_nums = []
    for num in numbers:
        if numbers.count(num) == 1:
            unique_nums.append(num)
    return unique_nums
print(return_unique([1, 9, 8, 8, 7, 6, 1, 6]))          
print(return_unique([5, 5, 2, 4, 4, 4, 9, 9, 9, 1]))  
print(return_unique([9, 5, 6, 8, 7, 7, 1, 1, 1, 1, 1, 9, 8])) 








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
    for name, age in people.items():    #item/key is name, age(number) is value
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












#Question 11
def count_repetitions(elements):
    counts = {}
    for item in elements: 
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts
print(count_repetitions(["cat","dog","cat","cow","cow","cow"]))  
print(count_repetitions([1, 5, 5, 5, 12, 12, 0, 0, 0, 0, 0, 0]))  
print(count_repetitions(["Infinity","null","Infinity","null","null"]))  







#Question 12
def items_purchased(store, wallet):
    affordable = []
    for item, price in store.items():
        if price <= wallet:
            affordable.append(item)
    return affordable
print(items_purchased({"Water": 1, "Bread": 3, "TV": 1000}, 300))  
print(items_purchased({"Apple": 4, "Pan": 100, "Spoon": 2}, 100))  
print(items_purchased({"Phone": 999, "Laptop": 5000, "PC": 1200}, 1))








#question 13
def total_sales(sales):
    total = 0
    for units in sales.values():
        total += units # add each products units to the total
    return total
print(total_sales({"Laptop": 5, "Phone": 10, "Tablet": 3}))  
print(total_sales({"Shoes": 20, "Hats": 15, "Jackets": 10}))  
print(total_sales({"Book": 1, "Pen": 2, "Notebook": 1})) 






# Question 14
def high_earners(employee_salaries, threshhold):
    result = []
    for employee, salary in employee_salaries.items():
        if salary > threshhold: 
            result.append(employee)
    return result
print(high_earners({"Alice": 50000, "Bob": 75000, "Charlie": 100000}, 60000))  
print(high_earners({"David": 30000, "Emma": 45000, "Frank": 50000}, 40000))    
print(high_earners({"George": 25000, "Hannah": 27000, "Ian": 29000}, 30000))
      









#Question 15
def total_donations(donations):
    total = 0
    for amount in donations.values():
        total += amount
    return total
print(total_donations({"John": 100, "Sarah": 200, "Mike": 50}))    
print(total_donations({"Anna": 500, "Tom": 1000, "Jerry": 1500}))     
print(total_donations({"Chris": 25, "Alex": 30, "Morgan": 45})) 









#Question 16
calories = {"apple": 95, "banana": 105, "orange": 62, "grape": 3, "pear": 102}
def total_calories(fruit_list):
    total = 0 
    for fruit in fruit_list:
        if fruit in calories:
            total += calories[fruit]
    return total
print(total_calories(["apple", "banana", "orange"]))         
print(total_calories(["grape", "grape", "grape", "grape", "grape"]))
print(total_calories(["banana", "pear", "apple"]))








#Question 17
prices = {
    "flour": 2.50,
    "sugar": 1.80,
    "eggs": 3.00,
    "milk": 2.00,
    "butter": 2.75,
    "vanilla": 4.50,
    "chocolate": 5.00
}
def total_cost(ingredients):
    total = 0 
    for ingredient in ingredients:
        if ingredient in prices:
            total += prices[ingredient]
    return total
print(total_cost(["flour", "sugar", "eggs", "butter"]))  
print(total_cost(["milk", "vanilla", "chocolate"]))      
print(total_cost(["eggs", "eggs", "flour", "sugar"]))








#Question 18 #############
def majority_element(nums):
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1  # count each number
    
    # find the number with the highest count
    for num, freq in count.items():
        if freq >= len(nums) / 2:  # majority condition
            return num

# Examples:
print(majority_element([3, 2, 3]))                 # → 3
print(majority_element([2, 2, 1, 1, 1, 2, 2]))     # → 2
print(majority_element([2, 2, 3, 2, 1, 2, 1, 4, 4, 1, 2, 2]))  # → 2


 



