import random

red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]

nums = range(37)

while True:
    num = nums[random.randint(0,36)]
    print(num)
    if num == 0:
        print('Zero was drawn!')
    else:
        if num < 18:
            print('Small')
        if num >= 18:
            print('Large')
        if num in red:
            print('Red')
        if num in black:
            print('Black')
        if num & 1:
           print('Odd')
        else:
           print('Even')

    print('----------------------------------------------------------------------')
    keystroke = input('Type <Enter> for Next Draw or <‘q’+Enter> for Finish ')
    if keystroke=='q':
        break
