# Eric Nuno
#Question 6



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

