# Eric Nuno
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
#for number in range(37, 1051):
   # if number % 2 == 0:
    #    print(number)


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

