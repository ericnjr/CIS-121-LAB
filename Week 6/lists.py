# examples
# write a function that takes a string as an argument and returns a dictionary containing all of the number of times each word was used in that string
my_words = '''there once was a traverse man who traveled very far and had an the man had an exquisite taste'''


def string_to_dictionary(word):
    string_as_list = word.split()
    word_dictionary = {}
    for word in string_to_list:
        if word in word_dictionary:
            word_dictionary[word] = word_dictionary[word] + 1
        else:
            word_dictionary[word] = 1
    return word_dictionary

print(string_to_dictionary(my_words))
x = string_to_dictionary(my_words)
for key in x:
    if len(key) >8:
        print(key)




phonebook = {'matt':5073891438, 'ashley':12345}
print(phonebook)
#to add to a dictionary, we use name_of_dict[ key ] = value
phonebook ['waters'] = 789
print(phonebook)
#to look up a value in a dictionary we use the name of dictionary and the key
print(phonebook['matt'])
#print(phonebook['martensen'])#doesn't work because not in dictionary
for person in phonebook.keys():     #returns all of the keys as a list
    print(person)                 #should print all of the names in the dictionary
for person in phonebook.keys():    
    print(person, phonebook[person])    # second thing return all of the phonenumbers in the dictionary     

#write a function that takes a string as an argument, and return a list containing all of the words that have at least two vowels.
def string_to_list_with_vowels(word):
    words = []
    built_word = ''
    vowel_count = 0
    #collect a word
    for letter in word:
        #print(letter, vowel_count, built_word)#can use to see where code is going wrong
        if letter == ' ':
            if vowel_count >= 2:
                words.append(built_word)# adds built word into the list if the amount of vowel is >=2
            built_word = '' 
            vowel_count = 0  # need to add this to reset vowel count to 0
        else:
            built_word += letter
            if letter in 'aeiou':
                vowel_count +=1
    if vowel_count >=2:
        words.append(built_word)        
    return words




# write a function that takes a string as an argument and returns a list containing all of the words in that string
my_word = 'Peter Piper picked a peck of pickled peppers'

def string_to_list(word):
    words = []
    built_word = ''
    #collect a word
    for letter in word:
        if letter == ' ':
            words.append(built_word)# adds built word into the list
            built_word = '' 
        else:
            built_word += letter
    words.append(built_word)        
    return words
    #once we have a full word, let's add it to the list of words
    
print(string_to_list(my_word))
    
def string_to_list(word):
    words = []
    built_word = ''
    for index in range(len(word)):
        if word[index] == ' ':
            word.append(built_word)
            built_word = ''
        elif index == len(word)-1:
            built_word += word[index]
        else:
            built_word += word[index]
        return words
#print(my_word,split())
#print(my_word.split(sep='e'))  #will split out the e from the word

  
# workdays = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday') #immutable tuple, people can't modify this data like they can a list in []


'''
lyst = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
#mutable object
x = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
y = x 
print(x)
print(y)
x[4] = 'Funday'
print(x)
print(y)


#immutable object

x = 'apple'
y = x
print(x)
print(y)

x += 's'
print(x)
print(y)


#print(lyst)
#lyst[4] = 'Funday'
#print(lyst)


#print(lyst[2][3:6]) # grabs wednesday and slices out nes

#for element in lyst:
 #   print(element)
    
    
#print(lyst)
#lyst.append('Saturday')    # append adds to the end of a list
#lyst.append('Sunday')
#print(lyst)


#print(x[2])
#print(x[1:4])

#in python, a list starts with a [ and ends with a ]
x = [] #this is a list with nothing in it.

lyst = ['apple', 'banana', 3,False, 4.5, 'grapes']
#print the element of the list in position 1.
print(lyst[1])
#print the portion of the list that is 3, False, and 4.5
print(lyst[2:5])

x = 'appl'
print(x)
x += 'e'
print(x)


#lyst.append ( element ) will add the element to the end of the lyst.

print(lyst)
lyst.append(12)
print(lyst)

print(lyst)
lyst.insert(3, 12)
print(lyst)
'''