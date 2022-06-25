# -*- coding: utf-8 -*-
"""
Hapsari
"""
def calculate():
    operation = input('''
+ for addition
- for subtraction
* for multiplication
/ for division

Please type in the math operation you would like to complete:''')
    try:
        num1 = int(input('Please enter the first number: '))
        num2 = int(input('Please enter the second number: '))
    except:
        print('Please input integer only')
        again()

    if operation == '+':
        print('{} + {} = '.format(num1, num2),num1 + num2)

    elif operation == '-':
        print('{} - {} = '.format(num1, num2), num1 - num2)

    elif operation == '*' or operation.upper() == 'X':
        print('{} * {} = '.format(num1, num2), num1 * num2)

    elif operation == '/':
        print('{} / {} = '.format(num1, num2), num1 / num2)

    else:
        print('You have not typed a valid operator, please run the program again ^^')
    
    again()

def again():
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('See you later.')
    else:
        print('You may have typed the wrong key, please read it again carefully ^^')
        again()

calculate()
