def main():
    Welcome()
    Arithemetic_operations()
    runAgain()
    End()
    
    
def Welcome():
    print("Welcome Genius!!")
 
def Arithemetic_operations():
    Operation = input('''
    What math problem would you want to solve today?
    "+" is for Addition
    "-" is for Subtraction
    "/" is for division
    "%" is for modulus
    "*" is for multiplication
    "**" if for power
    "0" to cancel operation
    ''')

    Num_1 = float(input('Please enter first number: '))
    Num_2 = float(input('Please enter second number: '))

    if Operation == '+':
        print('{} + {} =' . format(Num_1, Num_2))
        print(Num_1 + Num_2)

    elif Operation == '-':
        print('{} - {} =' . format(Num_1, Num_2))
        print(Num_1 - Num_2)

    elif Operation == '/':
        print('{} / {} =' . format(Num_1, Num_2))
        print(Num_1 / Num_2)

    elif Operation == '%':
        print('{} % {} =' . format(Num_1, Num_2))
        print(Num_1 % Num_2)

    elif Operation == '*':
        print('{} * {} =' . format(Num_1, Num_2))
        print(Num_1 * Num_2)
    elif Operation == '**':
        print('{} ** {} =' . format(Num_1, Num_2))
        print(Num_1 ** Num_2)
    elif Operation == "":
        End()
    else:
        print("You have entered an incorrect option. Please run again")

      
def End():
    print("Thank you for using Genius calculator. See you next time")
    
def runAgain():
    Calc_again = input('''
    Do you want to calculate again?
    y for Yes
    n for No
    ''')
    if Calc_again.upper() == 'Y':
        Arithemetic_operations()
    elif Calc_again.upper() == 'N':
        End()
        
    else:
        runAgain()
    
 
    
if __name__=="__main__":
    main()
    






