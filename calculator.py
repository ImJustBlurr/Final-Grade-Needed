reiterate = True

while reiterate == True:
    print('\nEnter your current grade (not including the final exam): ')
    current = float(input()) * .01

    print('\nEnter the grade you you want to end up with: ')
    desired = float(input()) * .01

    print('\nWhat is the weight of the final exam? (represented as a percentage): ')
    weight = float(input()) * .01

    gradeNeeded = ((desired - (1 - weight)*current)/weight) * 100
    print(f'\nYou need a {int(gradeNeeded)}% to achieve a {int(desired*100)}% overall.\n')

    choice = input('Would you like to continue? y/n\n')
    if choice.lower() == 'y':
        reiterate = True
    elif choice.lower() == 'n':
        reiterate = False