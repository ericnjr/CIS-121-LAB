
#print all of the odd numbers between 5 and some user given value
user_num = int(input('Enter a number: '))
for number in range(5, user_num+1,2):
    print(number)


#find the sum of user entered values until the user types q
sum = 0
user_number = input('Enter a number or type q to end: ')
while user_number != "q":
    sum += int(user_number)
    user_number = input('Enter a number or type q to end: ')
print(f'total = {sum}')

sum = 0
for number in range(10**9):
    user_number = int(input('enter number or q to end: '))
    if user_number == "q":
        break
    sum += user_number
    print(sum)





#print all of the even numbers between 1...10
for number in range(1,11):
    if number % 2 == 0:
        print(number)
    
# another way to do the evens, use the step feature(range(start,stop,step))
for number in range(2,11,2):
    print(number)




#print the numbers 1..10 with a for in range example
for number in range(1,10+1):
    print(number)
    


#while example
number = 1
while number <= 10:
    print(number)
    number+=1





#these are examples of loops
#write a program that adds numbers until the user says stop
total = 0 
user_number = input("enter a number or type q to end")
while user_number != "q":
    total += int(user_number)
    user_number = input("enter a number or type q to end")
print(f'total = {total}')






#print all even numbers that are not divisible by 3
number = 0 
while number < 50:
    number += 1
    if number % 2 == 0:
        if number % 3 == 0:
            #do nothing 
            #and skip the rest of the code
            continue
        print(number)
    



#print all the odd numbers between 5 and some number given by the user
upper = int(input('Enter a number: '))
start_num = 5
while start_num <= upper:
    if start_num % 2 == 1:
        print(start_num)
        start_num += 1






#print numbers 1 .. 10

number = 1

while number <= 10:
    print(number)
    number += 1

#print the even numbers between 1..10
number = 2
while number <= 10:
    print(number)
    number += 2
   
   
number = 1
while number <= 10:
    if number % 2 == 0:
        print(number)
    number += 1           # can put the control of the iteration anywhere in the loop body
