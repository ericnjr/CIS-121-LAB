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
#var_name = open('whatever your file name is . ext', 'w')

my_file = open('numbers.txt', 'w')

'''
my_file.write('Hello World!\n')
my_file.write('Hello World!')
'''
for index in range(0, 100):
    number = randint(50, 250)
    my_file.write(str(number)+ '\n')
