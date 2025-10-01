# examples
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