#problems done wrong
def is_isogram(word):
    if len(word) == len(set(word)):
        return True
    else:
        return False
print(is_isogram("algorithm"))
print(is_isogram("password"))


def highway_directions(highway_num):
    # Primary highways: 1–99
    if 1 <= highway_num <= 99:
        if highway_num % 2 == 0:
            return f"I-{highway_num} runs east/west"
        else:
            return f"I-{highway_num} runs north/south"
    
    # Auxiliary highways: 100–999
    elif 100 <= highway_num <= 999:
        primary = highway_num % 100
        # Must be a valid primary (1–99), not "00"
        if 1 <= primary <= 99:
            return f"I-{highway_num} is an auxiliary highway, serving I-{primary}"
        else:
            return f"I-{highway_num} is an invalid highway number"
    
    # Anything else is invalid
    else:
        return f"I-{highway_num} is an invalid highway number"