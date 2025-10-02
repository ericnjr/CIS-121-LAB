#problems done wrong
def is_isogram(word):
    if len(word) == len(set(word)):
        return True
    else:
        return False
print(is_isogram("algorithm"))
print(is_isogram("password"))


