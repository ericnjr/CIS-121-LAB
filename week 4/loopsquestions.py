# Eric Nuno
#Question 11
n = int(input('Enter an integer: '))
total = 0
for i in range (1,n + 1):
    total += i ** 2   
print(total)






#Question 10
largest_even = -1 #default is no even numbers entered
while True:
    num = int(input('Enter an integer(negative to stop): '))
    if num < 0:
        break
    if num % 2 == 0:
        if num > largest_even:
            largest_even = num
print(largest_even)

       






#9
width = int(input('Enter a width: '))
length = int(input('Enter a length: '))
pattern = input('Enter a single character pattern: ')
for _ in range(length):
    print(pattern * width)





#Question 8
n = int(input('Enter an integer: '))
print("Factors:", end=" ")
for i in range(1, n+1):
    if n % i == 0:
        print(i, end=" ")
print()





#Question 7
n = 25
while True:
    print(n, end= ' ')
    if n == 1:
        break
    if n % 2 == 0:
        n //= 2 
    else: 
        n = 3 * n + 1
print()





#Question 6
total = 0 
while True:
    num = int(input('Enter a numbe(negative to stop): '))
    if num < 0:
        break
    total += num
print(f'The sum = {total}')





#Question 5
sum = 0
for number in range(51, 518, 2):
    sum += number
print(sum)





#Question 4
word = ""
while True:
    user_in = input('Enter a letter: ')
    if user_in == "done":
        break
    else:
        word += user_in
print(f'The final word is {word}')








#Question 3
for number in range(37, 1051):
    if number % 2 == 0:
       print(number)


#Question 2
user_word = input('Enter a word: ')
result = ""
for i in range(1, len(user_word) - 1,2):
    result += user_word[i]
print(f' Output = {result}')


#Question 1
larger_num = int(input('Enter the larger number: '))
smaller_num = int(input('Enter the smaller number: '))
while larger_num > smaller_num:
    larger_num /= 2
    num += 1
print(f'Number of times halved: {num}')

