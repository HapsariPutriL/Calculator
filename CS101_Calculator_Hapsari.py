'''
Hapsari
'''
def calculate():
    operation = input('''
+  for addition
-  for subtraction
*  for multiplication
/  for division
** for power
%  for modulo

Please type in the math operation you would like to complete:''')
    try:
        num1 = int(input('Please enter the first number: '))
        num2 = int(input('Please enter the second number: '))
    except:
        print('Please input integer only')
        again()

    if operation == '+':
        print('{} ditambah {} = '.format(num1, num2),num1 + num2)

    elif operation == '-':
        print('{} dikurang {} = '.format(num1, num2), num1 - num2)

    elif operation == '*' or operation.upper() == 'X':
        print('{} dikali {} = '.format(num1, num2), num1 * num2)

    elif operation == '/':
        print('{} dibagi {} = '.format(num1, num2), num1 / num2)
        
    elif operation == '**' or operation == '^':
        print('{} pangkat {} = '.format(num1, num2), num1 ** num2)
        
    elif operation == '%':
        print('{} modulo {} = '.format(num1, num2), num1 % num2)

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
        print('See you later, bye bye ^^')
    else:
        print('You may have typed the wrong key, please read it again carefully ^^')
        again()

calculate()
