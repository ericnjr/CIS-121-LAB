# strings
#Question 1

def is_fever(temperature):

# how can we extract the F and C? hint word[-1]
    unit = temperature[-1]
# if it is F -> 98.6 is a fever
    if unit == "F":
        if float(temperature[:-1]) > 98.6:
            return True
        else:
            return False
#if it is c -> 37 is a fever        
    elif unit == "C":
        if float(temperature[:-1]) >37:
            return True
        else:
            return False

#input and print should be outside the function

user_input = input("Enter a temperature in F or C ")
print(f"Is fever ? {is_fever(user_input)}")


