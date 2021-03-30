def main():
    welcome()
    arithmetic_operations()
    run_again()
    end()


def welcome():
    print("Welcome Genius!!")


def arithmetic_operations():
    operation = input('''
    What math problem would you want to solve today?
    1 is for Addition
    2 is for Subtraction
    3 is for Division
    4 is for Modulus
    5 is for Multiplication
    6 if for Power
    0 to cancel operation
    ''')

    if operation != "0":
      num_1 = float(input('Please enter first number: '))
      num_2 = float(input('Please enter second number: '))

      if operation == '1':
        print('{} + {} ='.format(num_1, num_2))
        print(num_1 + num_2)

      elif operation == '2':
        print('{} - {} ='.format(num_1, num_2))
        print(num_1 - num_2)

      elif operation == '3':
        print('{} / {} ='.format(num_1, num_2))
        print(num_1 / num_2)

      elif operation == '4':
        print('{} % {} ='.format(num_1, num_2))
        print(num_1 % num_2)

      elif operation == '5':
        print('{} * {} ='.format(num_1, num_2))
        print(num_1 * num_2)

      elif operation == '6':
        print('{} ** {} ='.format(num_1, num_2))
        print(num_1 ** num_2)

      else:
        print("You have entered an incorrect option. Please run again")
    else:
      end()


def end():
    print("Thank you for using Genius calculator. See you next time")


def run_again():
    calc_again = input('''
    Do you want to calculate again?
    y for Yes
    n for No
    ''')

    while calc_again.upper() == 'Y':
      arithmetic_operations()
      run_again()
      
      if calc_again.upper() == 'N':
        end()
      break
    

if __name__ == "__main__":
    main()
