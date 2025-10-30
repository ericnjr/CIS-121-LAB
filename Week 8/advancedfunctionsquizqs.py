#Question 1
from random import randint

def toss_coin(guess=0):  #defaults guess to 0
    value = randint(0, 1) # picks a random integer. Either 0 or 1
    if guess == value:
        return "Correct!"
    else:
        return "Incorrect!"
print(toss_coin())     
print(toss_coin(0))  
print(toss_coin(1))    
   

    


#Question 2
from random import randint
def guess(guess="even"):  # defaults guess to even 
    value = randint(0, 9)
    result = "even" if value % 2 == 0 else "odd"
    return "Correct!" if guess == result else "Incorrect!"
print(guess())        
print(guess("odd"))  
print(guess("even"))


    
    




#Question 3
def count_duplicates(num1=0, num2=0, num3=0):  # defaults all numbers to 0
    nums = [num1, num2, num3]
    unique = set(nums)
    if len(unique) == 1:
        return "There are 3 of the same number"
    elif len(unique) == 2:
        return "There are 2 of the same number"
    else:
        return "Each number is unique"
print(count_duplicates(2, 3, 2))  
print(count_duplicates(4, 4, 4))  
print(count_duplicates(1, 2, 3))  
print(count_duplicates(1))        
print(count_duplicates(0))   
    

    



#Question 4
def find_winner(player1="rock", player2="rock"): #defaults all inputs to rock
    if player1 == player2:
        return "It's a tie!"
    elif (player1 == "rock" and player2 == "scissors") or \
         (player1 == "scissors" and player2 == "paper") or \
         (player1 == "paper" and player2 == "rock"):
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"
print(find_winner("rock", "paper"))      
print(find_winner("scissors", "paper"))  
print(find_winner("rock", "rock"))       
print(find_winner("rock"))              
print(find_winner())                     
print(find_winner("scissors"))  



 
    


#Question 5
def find_relation(name=""):
    if name == "Darth Vader":
        return "Father"
    elif name == "Leia":
        return "Sister"
    elif name == "Han":
        return "Brother in law"
    elif name == "R2D2":
        return "Droid"
    else:
        return "Unknown"
print(find_relation("Darth Vader"))   
print(find_relation("R2D2"))          
print(find_relation("Jabba the Hutt"))
print(find_relation()) 






#Question 6  ########
def hailstone_seq(n=40):
    sequence = []
    while n != 1:
        sequence.append(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    sequence.append(1) #adds the final 1
    print(",".join(map(str, sequence)))  #########
hailstone_seq(25) 
hailstone_seq(40)  
hailstone_seq()       







#Question 7
def ascending_order(num1, num2=5, num3=25):
    # Compare and swap to order numbers
    if num1 > num2:
        num1, num2 = num2, num1
    if num1 > num3:
        num1, num3 = num3, num1
    if num2 > num3:
        num2, num3 = num3, num2
    return [num1, num2, num3]
print(ascending_order(2, 3, 1))   
print(ascending_order(10, 1))     
print(ascending_order(50))





    


#Question 8
def descending_order(num1, num2=15, num3=5): #set defaults
    #compare and swap to get descending order
    if num1 < num2:
        num1, num2 = num2, num1
    if num1 < num3:
        num1, num3 = num3, num1
    if num2 < num3:
        num2, num3 = num3, num2
    return [num1, num2, num3]
print(descending_order(2, 3, 1))  
print(descending_order(10))        
print(descending_order(2, 45))





#Question 9  ##########
def get_indices(lst, value=0):
    indices = []
    for i in range(len(lst)):
        if lst[i] == value:
            indices.append(i)
    return indices
print(get_indices([1, 0, 5, 0, 7]))           
print(get_indices([1, 5, 5, 2, 7], 7))        
print(get_indices([1, 5, 5, 2, 7]))           
print(get_indices([1, 5, 5, 2, 7], 5))        
print(get_indices([1, 5, 5, 2, 7], 8))       
print(get_indices(["a","a","b","a","b","a"], "a"))










#Question 10  ######
def find_factors(num=36):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    print(", ".join(map(str, factors)))  #########
find_factors(12)  
find_factors(17)  
find_factors(36)  
find_factors()








#Question 11
def list_of_multiples(num, length=5):
    multiples = []
    for i in range(1, length+1):
        multiples.append(num * i)
    return multiples
print(list_of_multiples(7, 5))   
print(list_of_multiples(12, 10))  
print(list_of_multiples(2))







#Question 12
def is_even(num):
    return num % 2 == 0
def report_evens(numbers):
    evens = []
    for n in numbers:
        if is_even(n):
            evens.append(n)
    return evens
print(report_evens([4, 3, 12, 16, 8, 9, 25]))          
print(report_evens([6, 100, 3, 12, 16, 6, 9, 100]))     
print(report_evens([3, 99, 7, 13, 25]))







#Question 13
def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u']
def report_vowels(text):
    vowels = []
    for ch in text:  #ch refers to character
        if is_vowel(ch):
            vowels.append(ch)
    return vowels
print(report_vowels("apple"))        
print(report_vowels("banana"))       
print(report_vowels("run time error"))







#Question 14
def is_two_digit_number(num):
    return (10<= abs(num) <=99)
def report_two_digit_numbers(numbers):
    result = []
    for n in numbers:
        if is_two_digit_number(n):
            result.append(n)
    return result
print(report_two_digit_numbers([100, 57, 12, 1]))         
print(report_two_digit_numbers([121, 36, -19, -6, 0, 21])) 
print(report_two_digit_numbers([100, 7, 8437]))



#Question 15
def is_negative(num):
    return num < 0
def is_odd(num):
    return num % 2 != 0
def report_negative_odds(numbers):
    result = []
    for num in numbers:
        if is_negative(num) and is_odd(num):
            result.append(num)
    return result
print(report_negative_odds([100, -57, 12, 1, -36, -15]))      
print(report_negative_odds([121, -101, 36, -19, -6, 0, 21, -1])) 
print(report_negative_odds([-100, 7, 8437])) 







