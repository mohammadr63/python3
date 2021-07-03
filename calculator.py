#Welcome to the desired user
#Call the function
def welcome():
    print('''
    Welcome to Calculator
    ''')

# First we create a function called def
def calculate():

# Using the input () command and writing the appropriate message 
# for the user, we get the two integers she wants.    
    number_1 = int(input("Enter your the first number: "))
    number_2 = int(input("Enter your the second number: "))
# Once we have obtained two integers from the user,
#  we need to specify what operation the user wants to perform on the numbers
#  for calculation and mathematical operations.
#   Therefore, we receive the desired operator again with the input () command.
    operation = input('''
    Please type in the math operation you would like to complete:
    + for addition
    - for subtraction
    * for multiplication
    ** for power 
    %  for modulo
     / for division''')
    
# Now that we have the numbers and 
# operator that the user wants, we have to perform the user's 
# requested mathematical operations
#  on the numbers according to the input operator and using if, elif and else.
    if operation == '+':
        output_number = number_1 + number_2
        print( "{} + {} = {}" .format(number_1, number_2, output_number))
    elif operation == '-':
        output_number = number_1 - number_2
        print( "{} - {} = {}" .format(number_1, number_2, output_number))
    elif operation == '*':
        output_number = number_1 * number_2
        print( "{} * {} = {}" .format(number_1, number_2, output_number))
    elif operation == '/':
        output_number = number_1 / number_2
        print( "{} / {} = {}" .format(number_1, number_2, output_number))
    elif operation == '**':
        output_number = number_1 * number_2
        print( "{} ** {} = {}" .format(number_1, number_2, output_number))
    elif operation == '%':
        output_number = number_1 * number_2
        print( "{} % {} = {}" .format(number_1, number_2, output_number))
    else:
        print('You entered the mark incorrectly. Please try again.')

    again()
# Define again() function to ask user if they want to use the calculator again
def again():

    calc_again = input('''
    Do you want to calculate again?
    Please type Y for YES or N for NO.
    ''')

    # If user types Y, run the calculate() function
    if calc_again.upper() == 'Y':
        calculate()
    # If user types N, say good-bye to the user and end the program
    elif calc_again.upper() == 'N':
        print('See you later.')
    # If user types another key, run the function again
    else:
        again()


#Call function welcome
welcome()

#  calculate() outside of the function
calculate()

