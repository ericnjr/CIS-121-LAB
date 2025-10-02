#problems done wrong
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

height = int(input("Enter the triangle height: "))

# Build the triangle
for i in range(1, height + 1):
    print("*" * i)




