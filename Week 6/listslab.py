#Eric Nuno
#Question 4
def output_odd(smaller, larger):
    odds = []
    for number in range(smaller, larger+1):
        if number % 2 != 0:
            odds.append(number)
    return odds





#Question 5
def hailstone_sequence(number):
    output_list = [number]
    while number != 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = number * 3 + 1
        output_list.append(number)
    return output_list
print(hailstone_sequence(25))



#Question 9
def count(cards):
    values = {
        2: 1, 3: 1, 4: 1, 5: 1, 6: 1,   # low cards  #dictionary
        7: 0, 8: 0, 9: 0,               # neutral cards
        10: -1, "j": -1, "q": -1, "k": -1, "a": -1  # high cards
    }

    total = 0
    for card in cards:
        total += values[card]   # look up card in dictionary and add
    return total

print(count([5, 9, 10, 3, "j", "a", 4, 8, 5]))      
print(count(["a", "a", "k", "q", "q", "j"]))        
print(count(["a", 5, 5, 2, 6, 2, 3, 8, 9, 7]))



#Question 19
def is_acronym(s, words):
    if len(s) != len(words):   # sees if the lengths match, abc, apples bananas, carrots
        return False
    acronym = ""
    for word in words:
        if not word:   #empty string check
            return False
        acronym += word[0]
    return acronym == s   #checks if acronym built matches the string s therefor returning True
print(is_acronym("abc", ["alice", "bob", "charlie"]))
print(is_acronym("a", ["an", "apple"]))                
print(is_acronym("ngguoy", ["never", "gonna", "give", "up", "on", "you"]))  
print(is_acronym("ab", ["apple", "banana", "cat"]))     
print(is_acronym("ab", ["apple", "", "cat"])) 




