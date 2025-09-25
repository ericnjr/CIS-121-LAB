#write a function that returns the product of two arguments.
def product(num1, num2):
    product = num1 * num2
    return product
print(product(4, 3))







#write a funtion that takes an interger, adds two then multiplys by 4 and prints the result
def my_function(number):
    number += 2
    number *= 4
    return number


result = 10
for number in range(0,10):
    result = my_function(result)
print(result)

def add_ten(number):
    number +=10
    return number

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^starting with the value 10, add 2 then multiply it by 4, take the result and add two to it, then mulitply by 4 again.
#call the function my_function 10 times.
#call the function my_function 100 times.
result1 = add_ten(my_function(10))
result2 = my_function(result1)
print(result2)




#wrtie code to determine how many vowels are in a given word
def vowel_counter(passed_word):
    vowels = ('aeiou')
    count = 0
    for letter in passed_word:
        if letter in vowels:
            count+= 1
    print(f" The vowel count in '{passed_word}' is {count}")
word1 = 'hello wolrd'
word2 = 'apples and bananas'
word3 = 'happy times'

vowel_counter('hello world')
vowel_counter('apples and bananas')
vowel_counter('happy times')







vowels = ('aeiou')
word = (input('Enter a word: '))
count = 0
for letter in word:
    if letter in vowels:
        count+= 1
print(f"The vowel count in '{word}' is {count}")






#write code to determine how many letter are in a word
word = "hello world"
count = 0
for letter in word:
    if letter != " ":
        count +=1 
print(f'The {word} has {count} letter in the word')

   
