'''
#example
print('Starting Program')


try:
    age = int(input('What is your age?:'))
    print(f'your age is {age}')
    print(f' next year your age will be {age + 1}') 
except ValueError:
    print('you must pick an integer age')

print("Your program ended normally")

'''
#another example
print("Enter a number. I will divide 10 by that number, and output the result")

user_input = input("pick a number:")

done = False

while not done:
    try: 
        user_number = int(user_input)
        result = 10 / user_number
        print(f'The result is {result}')
        done = True
    except ValueError:
        print("please pick an integer")
        user_input = input("pick a number:")
    except ZeroDivisionError:
        print('You cannot divide by 0')
        user_input = input("pick a number:")

print("The end")



