width = int(input('Enter a width: '))
length = int(input('Enter a length: '))
pattern = input('Enter a single character pattern: ')
for _ in range(width):
    print(pattern * length)
