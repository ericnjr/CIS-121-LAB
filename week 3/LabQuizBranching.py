#19
name = input('Enter name: ')
if name == "Darth Vader":
    print('Father')
elif name == "Leia":
    print("Sister")
elif name == "Han":
    print("Brother in Law")
elif name == "R2D2":
    print("Droid")
else:
    print("Unknown")
    



#18
length_one = int(input('Enter a side lenth:'))
length_two = int(input('Enter a side lenth:'))
length_three = int(input('Enter a side lenth:'))
if length_one == length_two == length_three:
    print('equilateral triangle')
elif length_one == length_two or length_one == length_three or length_two == length_three:
    print('isosceles triangle')
else:
    print('scalene triangle')
    
#17
player_one = input('Enter rock, paper or scissors: ')
player_two = input('Enter rock, paper or scissors: ')
if player_one == player_two:
    print("It's a tie!")
elif (player_one == "rock" and player_two == "scissors") \
or (player_one == "paper" and player_two == "rock") \
or (player_one == "scissors" and player_two == "paper"):
    print('Player one wins!')
elif (player_two == "rock" and player_one == "scissors") \
or (player_two == "paper" and player_one == "rock") \
or (player_two == "scissors" and player_one == "paper"):
    print('Player two wins!')
else:
    print('Invalid input')



#16
flavor = input('Pcik a flavor: ')
if flavor == "Vanilla":
    print('Here is your vanilla ice cream!')
elif flavor == "Chocolate":
    print('Here is your chocolate ice cream!')
elif flavor == "Strawberry":
    print('Here is your strawberry ice cream')
else:
    print(f' sorry we don not have {flavor} ice cream')



#15
age = int(input('Enter age: '))
time = input('Enter Morning or Afternoon: ')
if age >= 1 and age <= 3:
    if time == "Morning":
        print('The pool is open at 9 AM')
    else:
        print('The pool is open at 1 PM')
elif age >= 4 and age <= 8:
    if time == "Morning":
        print('The pool is open at 10 AM')
    else:
        print('The pool is open at 2 PM')
elif age >= 9 and age <= 12:
    if time == "Morning":
        print('The pool is open at 11 AM')
    else:
        print('The pool is open at 3 PM')
else:
    print('Invalid age entered')



#14
letter = input('Enter a letter:')
if letter in "aeiou":
    print('Vowel')
else:
    print('Constanant')


#13(look over)
highway = int(input('Enter highway number'))
if highway >= 1 and highway <= 99:
    if highway % 2 == 0:
        print(f'highway {highway} runs east/west.')
    else:
        print(f'highway {highway} runs north/south')
elif highway >=100 and highway <= 999:
    primary = highway % 100
    if primary == 0 or not (1 <= primary <= 99):
        print('Invalid highway number entered')
    else:
        direction = "east/west" if primary % 2 == 0 else "north/south"
        print(f'highway {highway} runs {direction}')
else:
    print('Invalid highway number entered')
    12



#12
int_1 = int(input('Enter an integer: '))
int_2 = int(input('Enter an integer: '))
int_3 = int(input('Enter an integer: '))
if int_1 == int_2 == int_3:
    print('You entered the same number 3 times')
elif int_1 == int_2 or int_1 == int_3 or int_2 == int_3:
    print('You entered the same number 2 times')
else:
    print('Each number is unique')


#11(redo)
from random import randint
value = randint(0,1) #picks a random integer. Either 1 or 0
guess = input('Enter heads or tails: ')
if value == 0:
    coin = "heads"
else:
    coin = "tails"
if guess == coin:
    print(f'Correct! It was {coin}')
else:
    print(f'Incorrect is was {coin}')




#10
race = input('Enter a race: ')
classs = input('Enter a class: ')
health_points = 0  #set initial value
if classs == "Warrior":
    if race =="Elf":
        health_points = 150
    elif race == "Ogre":
        health_points = 200
    else:
        print('Invalid race entered')

elif classs == "Bard":
    if race == "Elf":
        health_points = 75
    elif race == "Ogre":
        health_points = 100
    else:
        print('Invalid race entered')
elif classs == "Wizard":
    if race =="Elf":
        health_points = 25
    elif race == "Ogre":
        health_points = 50
    else:
        print('Invalid race entered')
else:
    print('Invalid class Entered')
if health_points > 0:
    print(F'You have {health_points} health points.')





#9
number_1 = float(input('Enter a number: '))
number_2 = float(input('Enter another number: '))
number_3 = float(input('Enter another number: '))
if number_1 < number_2 and number_1 < number_3:
    print(number_1)
elif number_2 < number_1 and number_2 < number_3:
    print(number_2)
else:
    print(number_3)



#8
number_1 = float(input('Enter a number: '))
number_2 = float(input('Enter another number: '))
number_3 = float(input('Enter another number: '))
if number_1 > number_2 and number_1 > number_3:
    print(number_1)
elif number_2 > number_1 and number_2 > number_3:
    print(number_2)
else:
    print(number_3)




#7
total_knuts = int(input('Enter total knuts: '))
#conversion rates
knuts_per_sickle = 29
sickle_per_galleon = 17
knuts_per_galleon = knuts_per_sickle * sickle_per_galleon

galleons = total_knuts // knuts_per_galleon
remaining_knuts = total_knuts % knuts_per_galleon
sickles = remaining_knuts // knuts_per_sickle
knuts = remaining_knuts % knuts_per_sickle

if galleons > 0:
    print(f'{galleons} galleon{'s' if galleons > 1 else ' '}')
if sickles > 0:
    print(f'{sickles} sickle{'s' if sickles > 1 else ' '}')
if knuts > 0:
    print(f'{knuts} knut{'s' if knuts > 1 else ' '}')



#6
int_1 = int(input('Enter a number: '))
int_2 = int(input('Enter another number: '))
int_3 = int(input('Enter another number: '))
if int_1 > int_2 and int_1 > int_3:
    if int_2 > int_3:
        print(int_1, int_2, int_3)
    else:
        print(int_1, int_3, int_2)
elif int_2 > int_1 and int_2 > int_3:
    if int_1 > int_3:
        print(int_2, int_1, int_3)
    else:
        print(int_2, int_3, int_1)
else:
    if int_1 > int_2:
        print(int_3, int_1, int_2)
    else:
        print(int_3, int_2, int_1)



#5
int_1 = int(input('Enter a number: '))
int_2 = int(input('Enter another number: '))
int_3 = int(input('Enter another number: '))
if int_1 < int_2 and int_1 < int_3:
    if int_2 < int_3:
        print(int_1, int_2, int_3)
    else:
        print(int_1, int_3, int_2)
elif int_2 < int_1 and int_2 < int_3:
    if int_1 < int_3:
        print(int_2, int_1, int_3)
    else:
        print(int_2, int_3, int_1)
else:
    if int_1 < int_2:
        print(int_3, int_1, int_2)
    else:
        print(int_3, int_2, int_1)



#4
age = int(input('Enter age: '))
goal = input('Enter Athleticism Goal, Above Average or Below Average: ')
if age >= 20 and age <= 39:
    if goal == "Above Average":
        print('Your resting heart rate should be between 47-72.')
    elif goal == "Below Average":
        print('73-93')
    else:
        print('Invalid goal') 
elif age >= 40 and age <= 59:
    if goal == "Above Average":
        print('Your resting heart rate should be between 46-71.')
    elif goal == "Below Average":
        print('Your resting heart rate should be between 72-94.')
    else:
        print('Invlaid goal')
elif age >= 60 and age <= 79:
    if goal == "Above Average":
        print('Your resting heart rate should be between 45-70')
    elif goal == "Below Average":
        print('Your resting heart rate should be between 71-97')
    else:
        print('Invalid goal')
else:
    print('Invalid age entered')




#3
light_color = input('Enter light color: ').strip().lower()
if light_color == "red":
    print('Stop')
elif light_color == "yellow":
    print("yield")
elif light_color == "green":
    print("go")
else:
    print("Invalid light color")

