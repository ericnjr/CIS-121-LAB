#more about functions
def add_three(x):
    y = x + 3
    return y
var0 = 7
var1 = add_three(var0)
print(var1)




#more dictionary examples
#write a function that returns a dictionary containing how many times each letter appears.
#result should look something like this d = {'p':9, 'e':}
def letter_counter(word):
    letter_dictionary = {}
    for letter in word:
        if letter in letter_dictionary:
            letter_dictionary[letter] += 1#add in key value pair. what are key and value?(if already in dictionary and seen again adds 1 to key)
        else: #key is not in dictionary
            letter_dictionary[letter] = 1 #adds in key value pair, sets equal t 1(seen it once)
    return letter_dictionary

my_word = 'peter piper picked a peck of pickled peppers'
letter_dict = letter_counter(my_word)
for letter in letter_dict:
    print(letter, letter_dict[letter])
#prints in an easier way to see


