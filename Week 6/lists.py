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
