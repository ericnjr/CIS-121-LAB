# strings

#Question 9
def flip_flop(word):
    mid = len(word) // 2
    first_half = word[:mid]
    second_half = word[mid:]
    return second_half + first_half
print(flip_flop("abcde"))


 


#Question 8
def last_letters(sentence):
    words = sentence.split()
    result = ""
    for word in words:
        result += word[-1] #[-1] adds the last letter of each word
    return result
print(last_letters("wingardium leviosa makes objects float"))


#Question 7
def first_letters(sentence):
    words = sentence.split() #splits sentence into words
    result = ""
    for word in words:
        result += word[0]
    return result
print(first_letters("wingardium leviosa makes objects float"))



#Question 6
def get_drinkn_ID(flavor, capacity):
    return flavor[:3] + str(capacity) #must string so it changes from number to string
print(get_drinkn_ID("apple", 500))



#question 5
def is_isogram(word):
    return len(word) == len(set(word))#set removes duplicates
print(is_isogram("algorithm"))
print(is_isogram("password"))



#Question 4
def hamming_distance(string1, string2):
    distance = 0
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            distance +=1
    return distance
print(hamming_distance("abcde", "bcdef"))
print(hamming_distance("strong","strung"))



#Question 3
def is_boiling(temperature):
    if temperature[-1] == "F":
        if float(temperature[:-1]) >= 212:
            return True
        else:
            return False
    elif temperature [-1] == "C":
        if float(temperature[:-1]) >= 100:
            return True
        else:
            return False
print(is_boiling("212F"))
print(is_boiling("100C"))
print(is_boiling("0F"))


#Question 2
def is_fever(temperature):
    if temperature[-1] == "F":
        if float(temperature[:-1]) >= 98.6: #[:-1] gives us ebverything except the last character
            return True
        else: 
            return False
    elif (temperature[-1]) == "C":
        if float(temperature[:-1]) > 37:#[:-1] gives us ebverything except the last character
            return True
        else:
            return False
print(is_fever("99F"))
print(is_fever("37C"))
print(is_fever("98F"))

#Question 1
def reverse_string(word):
    return word[::-1] # this slices the string from start to end but steps backwards effectively reversing it
print(reverse_string('programming'))
print(reverse_string('python'))
print(reverse_string('hello'))







    







    
        

        


