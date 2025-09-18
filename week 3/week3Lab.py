name = input("Enter a name: ").strip().title()

# Check the name and print the relation
if name == "Darth Vader":
    print("Father")
elif name == "Leia":
    print("Sister")
elif name == "Han":
    print("Brother in law")
elif name == "R2D2":
    print("Droid")
else:
    print("unknown")
    


from random import randint

value = randint(0, 1)
guess = input("Guess the coin flip! Enter 'heads' or 'tails': ")

if value == 0:
    coin = "heads"
else:
    coin = "tails"

if guess == coin:
    print(f"Correct! It was {coin}.")
else:
    print(f"Incorrect. It was {coin}.")






#6 question on branching lab q's
total_knuts = int(input("Enter the number of knuts: "))

# Conversion rates
KNUTS_PER_SICKLE = 29
SICKLES_PER_GALLEON = 17
KNUTS_PER_GALLEON = SICKLES_PER_GALLEON * KNUTS_PER_SICKLE

# Calculate galleons, sickles, and knuts
galleons = total_knuts // KNUTS_PER_GALLEON
remaining_knuts = total_knuts % KNUTS_PER_GALLEON

sickles = remaining_knuts // KNUTS_PER_SICKLE
knuts = remaining_knuts % KNUTS_PER_SICKLE

# Print only non-zero values
if galleons > 0:
    print(f"{galleons} galleon{'s' if galleons > 1 else ''}", end=" ")
if sickles > 0:
    print(f"{sickles} sickle{'s' if sickles > 1 else ''}", end=" ")
if knuts > 0:
    print(f"{knuts} knut{'s' if knuts > 1 else ''}")
