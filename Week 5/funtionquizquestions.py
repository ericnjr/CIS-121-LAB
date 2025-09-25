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


def pyramid_volume(base, height):
    volume = (base**2 * height)/3
    return volume
print(f"The volume of the pyramid is {pyramid_volume(3, 4)}")

#question 8



def pool_times(grade, time):
    pool_time = " "
    if grade == "k":
        grade = 0


    if 0 <= int(grade) <= 3:
        if(time == "morning"):
            pool_time = "9am"
        else:
            pool_time = "1pm"
    elif grade( 4 < int(grade <=8)):
        if(time == "morning"):
            pool_time = "10am"
        else:
            pool_time = "2pm"
    elif grade(9 < int(grade) <= 12):
        if(time == "morning"):
            pool_time = "11am"
        else:
            pool_time = " 3pm"
    return pool_time


print(f"Pool time is: { pool_times('k', 'morning') }")

#question 11
def convert_knuts(knuts):
    #knuts, sickles, galleons

    #1. for the number of knuts that i have how many galleons can i buy?
    galleons = knuts // (29 * 17)
    remaining_knuts = knuts - (galleons* (29 * 17))
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






