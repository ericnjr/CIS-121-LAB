
#Question 24
def skip_lettet(word):
    result = ""
    for i in range(1, len(word)-1, 2):
        result += word[i]
    return result
print(skip_lettet("counterattack"))


#Question 27
def odd_sum(smaller_num, larger_num):
    sum = 0
    for number in range(smaller_num, larger_num +1):
        if number % 2 != 0:
            sum += number
    return sum 
print(odd_sum(0, 7))


#Question 29
def sum_loop():
    sum = 0
    while True:
        user_number = int(input('Enter a number or type a negative to end: '))
        if user_number < 0:
            break
        else:
            sum += user_number
    return sum
print(f'The total sum is: {sum_loop()}')


#Question 30
def hailstone_seq(n):
    sequence = []
    while True:
        sequence.append(n)
        if n == 1:
            break
        if n % 2 == 0:
            n//=2
        else:
            n = 3 * n + 1
    return sequence
print(hailstone_seq(25))

#Question 31
def find_factors(number):
    factors = []
    for i in range(1, number +1):
        if number % i == 0:
            factors.append(i)
    return factors
print(find_factors(12))
# Question 34
def cube_sum(n):
    sum = 0
    for i in range(1, n+1):
        sum += i ** 3
    return sum
print(cube_sum(3))











# Question 22
def check_name(name):
    if name == "Darth Vader":
        return 'Father'
    elif name == "Leia":
        return "Sister"
    elif name == "Han":
        return "Brother in Law"
    elif name == "R2D2":
        return "Droid"
    else:
        return "Unknown"
print(check_name("Han"))





#Question 28
def create_word():
    word = ""
    while True:
        letter = input("Enter letter: ")
        if letter == "done":
            break
        else:
            word += letter
    return word
print(f"The final word is: {create_word()}")




#Question 32
def design_rug(width, length, pattern):
    rug = ""
    for _ in range(length):
        rug += (pattern * width) + "\n"
    return rug
print(design_rug(3, 5, "$"))

        



#Question 17
def check_letter(letter):
    vowels = ('aeiou')
    if letter in vowels:
        return "vowel" 
    else:
        return "constonant"
print(f'Is a vowel? {check_letter("z")}')
    


#Question 5
def legs_of_animals(chickens, cows, pigs):
    total_legs = (chickens * 2) + ( cows * 4) + (pigs * 4)
    return total_legs
print(f'The total number of legs is {legs_of_animals(2, 4, 4)}')





# Question 2
import math
def cone_volume(radius, height):
    volume = math.pi * ((radius**2) * height)/3
    return volume
print(f'The volume of the cone is {cone_volume(1,2)}')



#question 14
from random import randint

def guess_num(user_guess):
    output = ""
    value = randint(0,9)
    if user_guess == "even":
        if value % 2 == 0:
            output = "correct"
        else:
            output = "incorrect"
    elif user_guess == "odd":
        if value % 2 != 0:
            output = "correct"
        else:
            output = "incorrect"

    return output


user_input = input("guess the random number , odd or even :")
print(f"The guess is : {guess_num(user_input)}")
#Question 1

def pyramid_volume(base, height):
    volume = (base**2 * height)/3
    return volume
print(f"The volume of the pyramid is {pyramid_volume(3, 4)}")

#question 8(LOOK OVER)
def pool_times(grade, time):
    pool_time = " "
    if grade == "k":
        grade = 0


    if 0 <= int(grade) <= 3:
        if(time == "morning"):
            pool_time = "9am"
        else:
            pool_time = "1pm"
    elif  4 <= int(grade) <=8:
        if time == "morning":
            pool_time = "10am"
        else:
            pool_time = "2pm"
    elif 9 <= int(grade) <= 12:
        if time == "morning":
            pool_time = "11am"
        else:
            pool_time = " 3pm"
    return pool_time


print(f"Pool time is: { pool_times('k', 'morning') }")

#question 11(LOOK OVER)
def convert_knuts(knuts):
    #knuts, sickles, galleons

    #1. for the number of knuts that i have how many galleons can i buy?
    galleons = knuts // (29 * 17)
    remaining_knuts = knuts % (29*17)
    #2. remianing knuts, how many sickles can i buy?
    sickles = remaining_knuts // 29
   
    #3. how many remaining knuts after buying sickles ?
    knuts = remaining_knuts % 29

    output = ""
    if galleons > 0:
        output += f"Galleons: {galleons} "
    if sickles > 0:
        output += f"Sickles: {sickles} "
    if knuts > 0:
        output += f"Knuts: {knuts} "
    

    return output
print(convert_knuts(32))



def pool_times(grade, time):
    if grade == "k":
        grade = 0
    pool_time = ''
    if 0 <= int(grade) <= 3:
        if time == "Morning":
            pool_time = '9AM'
        else:
            pool_time = '1PM'
    return pool_time







