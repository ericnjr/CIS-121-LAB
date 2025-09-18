standards_met = int(input('Enter your standard: '))

if standards_met == 57:
    print('A+')
elif standards_met >= 53 and standards_met < 57:
    print('A')
elif standards_met >= 51 and standards_met < 53:
        print('A-')
if standards_met >= 45 and standards_met < 51:
    if standards_met >=49 and standards_met < 51:
                print('B+')
    elif standards_met >= 47 and standards_met < 49:
                print('B')
    elif standards_met >=45 and standards_met < 47:
                print('B-')
    if standards_met >= 40 and standards_met < 45:
        if standards_met >= 43 and standards_met < 45:
                print('C')
        elif standards_met >= 40 and standards_met <43:
                print('C-')
    if standards_met >= 35 and standards_met < 40:
        if standards_met >= 35 and standards_met < 40:
                print('D')
        elif standards_met < 35:
                print('F')
