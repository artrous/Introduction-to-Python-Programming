#Rolling Dice

import random
dice1 = range(7)
dice2 = range(7)

while True:
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    print(dice1, end='     ')
    print(dice2)   

    print('----------------------------------------------------')
    keystroke = input('Type <Enter> for Next Dice or <‘q’+Enter> for Finish ')
    if keystroke=='q':
        break
