#Eric Nuno
#Question 1
def skip_letter(word):
    return[letter for letter in word[::2]] #use slicing eith a step of 2 to get every other letter starting from index 0
print(skip_letter("counterattack"))
print(skip_letter("banana sunday"))








#Question 2
def skip_letter(word):
    return[letter for letter in word[1::2]]#use slicing to start at index 1, take every 2nd character
print(skip_letter("counterattack"))
print(skip_letter("banana sunday"))








#Question 3
def output_evens(smaller, larger):
    evens = []
    for number in range(smaller,larger+1):
        if number % 2 == 0:
            evens.append(number)
    return evens
print(output_evens(37, 1050))













#Question 4
def output_odd(smaller, larger):
    odds = []
    for number in range(smaller, larger+1):
        if number % 2 != 0:
            odds.append(number)
    return odds
print(output_odd(37, 1050))











#Question 5
def hailstone_seq(number):
    sequence = [number]
    while number != 1: 
        if number % 2 == 0:
            number = number // 2
        else:
            number = 3 * number +1
        sequence.append(number)
    return sequence
print(hailstone_seq(25))









#Question 6
def find_factors(number):
    factors = []
    for i in range(1,number +1):
        if number % i == 0:
            factors.append(i)
    return factors
print(find_factors(12))
print(find_factors(17))
print(find_factors(36))













 #Question 7
def ascending_order(num1, num2, num3):
    if num1 > num2:  
        num1, num2 = num2, num1 #swap if nunber1 is greater
    if num2 > num3:
        num2, num3 = num3, num2 #swap if number2 is greater
    if num1 > num2:
        num1, num2 = num2, num1
    return [num1, num2, num3]
print(ascending_order(2, 3, 1))    
print(ascending_order(10, 1, 25))  
print(ascending_order(2, 45, 4))








#Question 8
def descending_order(num1, num2, num3):
    if num1 < num2:
        num1, num2 = num2, num1
    if num2 < num3:
        num2, num3 = num3, num2
    if num1 < num2:
        num1, num2 = num2, num1
    return [num1, num2, num3]
print(descending_order(2, 3, 1))    
print(descending_order(10, 1, 25))  
print(descending_order(2, 45, 4))








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










#Question 10
def war_of_numbers(numbers):
    even_sum = 0
    odd_sum = 0
    for num in numbers:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num
    if even_sum > odd_sum:
        return "evens"
    elif odd_sum > even_sum:
        return "odds"
    else:
        return "tie"
print(war_of_numbers([2, 8, 7, 5]))        
print(war_of_numbers([12, 90, 75, 1, 1])) 
print(war_of_numbers([2, 10, 22, 243]))    
    







#Question 11
def add_lists(lyst1, lyst2):
    result = []
    for i in range(len(lyst1)):
        result.append(lyst1[i] + lyst2[i])
    return result
print(add_lists([1, 3, 3, 1], [4, 3, 6, 1]))      
print(add_lists([1, 8, 5, 0, -7], [0, -7, 4, 2, -6])) 
print(add_lists([1, 2], [-1, 1])) 














#Question 12
def largest_even(numbers):
    largest = -1 #default if no number is found
    for num in numbers:
        if num % 2 ==0:
            if largest == -1 or num > largest: #compare with current largest
                largest = num
    return largest
print(largest_even([3, 7, 2, 1, 7, 9, 10, 13]))  
print(largest_even([1, 3, 5, 7]))                
print(largest_even([0, 19, 18973623]))









#Question 13
def largest_odd(numbers):
    largest = -1 #default if no number is found
    for num in numbers:
        if num % 2 != 0:
            if largest == -1 or num > largest: #compare with current largest
                largest = num
    return largest
print(largest_odd([3, 7, 2, 1, 7, 9, 10, 13]))  
print(largest_odd([2, 4, 6, 8]))                
print(largest_odd([0, 19, 18973623]))








#Question 14
def progress_days(miles):
    count = 0
    for i in range(1,len(miles)):
        if miles[i] > miles[i-1]:
            count += 1
    return count
print(progress_days([3, 4, 1, 2]))    
print(progress_days([10, 11, 12, 9, 10])) 
print(progress_days([6, 5, 4, 3, 2, 9]))  
print(progress_days([9, 9]))
 







#Question 15
def lag_days(miles):
    count = 0
    for i in range(1,len(miles)):
        if miles[i] < miles[i-1]:
            count += 1
    return count
print(lag_days([5, 3, 2, 1]))    
print(lag_days([10, 11, 12, 9, 10])) 
print(lag_days([6, 5, 4, 3, 2, 9]))  
print(lag_days([9, 9]))









#Question 16
def like_or_dislike(events):
    state = "nothing"
    for event in events:
        if state == event:
            state = "nothing"
        else:
            state = event
    return state
print(like_or_dislike(["dislike"]))                  
print(like_or_dislike(["like", "like"]))         
print(like_or_dislike(["dislike", "like"]))         
print(like_or_dislike(["like", "dislike", "dislike"]))










#Question 17
def get_indices(lst, item):
    indices = []
    for i, value in enumerate(lst):
        if value == item:
            indices.append(i)
    return indices
print(get_indices([1, 5, 5, 2, 7], 7))    
print(get_indices([1, 5, 5, 2, 7], 5))          
print(get_indices([1, 5, 5, 2, 7], 8))         
print(get_indices(["a","a","b","a","b","a"], "a")) 











#Question 18
def list_of_multiples(num, length):
    multiples = []
    for i in range(1, length +1):
        multiples.append(num * i)
    return multiples
print(list_of_multiples(7, 5))    
print(list_of_multiples(12, 10))  
print(list_of_multiples(17, 6))













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




