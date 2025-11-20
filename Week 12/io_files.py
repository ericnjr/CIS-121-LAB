#wrtie a program that takes integers from the user and adds them together until they type done, return sum
'''
total = 0 
user_input = input("Enter a number or done to stop: ")

while user_input != 'done':
    user_number = float(user_input)
    total += user_number
    user_input = input("Enter a number or done to stop: ")

print(f'total = {total}')
'''

from random import randint
#var_name = open('whatever your file name is . txt', 'w')
'''
my_file = open('numbers.txt', 'w')


my_file.write('Hello World!\n')
my_file.write('Hello World!')
'''
'''
for index in range(0, 100):
    number = randint(50, 250)
    my_file.write(str(number)+'\n')



my_file.close()
'''
'''
my_file = open('numbers.txt', 'r')

data = my_file.readlines()

total = 0
count = 0
for line in data:
    number = float(line)
    total += number
    count += 1
print(f'total = {total}')
print(f'avg = {total/count}')
'''


new_file = open('family.txt', 'w')

new_file.write('Name,Age,Occupation,Hobby\n')
new_file.write('Matt,39,Teacher,Running\n')
new_file.write('Dexter,8,Student,Reading\n')
new_file.write('Ashley,38,Important Teacher,Learning\n')

new_file.close()




my_file = open('family.txt', 'r')
total = 0
count = 0

data = my_file.readlines()
for line in data[1:]:
    line_data = line.split(",")
    name = line_data[0]
    occupation = line_data[2]  
    age = float(line_data[1])
    total += age
    count += 1
    
    print(f"{name} is a {occupation}")

print(f'avg = {total/count}')
