print('ALWAYS ACT LIKE A KING')
print('-----')

# A student attended a university examination
# The marks the student obtained in various subjects are stored in a list like this:

marks = [60, 70, 65, 75, 80]

# EXPECTION: Get the average marks obtained in the exam, and, based on the average marks find the grade

# grade rule
# --- The student gets Grade A if the average marks is equal to or above 80
# --- The student gets Grade B if the average marks is equal to or above 60 and less than 80
# --- The student gets Grade C if the average marks is equal to or above 50 and less than 60
# --- The student gets Grade F if the average marks is less than 50

# define function to find average mark
def find_average_mark(marks):
    sum_of_marks = sum(marks)
    total_subject = len(marks)
    average_mark = sum_of_marks / total_subject
    return average_mark

# function call 
marks = [60, 70, 65, 75, 80]
average_mark = find_average_mark(marks)
print('The average mark is:', average_mark)
print('-----')

# define function to calculate the grade and return it
def compute_grade(average_mark):
    if average_mark >= 80:
        grade = 'A'
    elif average_mark >= 60:
        grade = 'B'
    elif average_mark >= 50:
        grade = 'C'
    else:
        grade = 'F'
    return grade

# fuction call
marks = [60, 70, 65, 75, 80]
average_mark = find_average_mark(marks)
print('The average mark is:', average_mark)

grade = compute_grade(average_mark)
print('The grade is:', grade)
print('-----')


# create a simple python calculator
print('Welcome to the python Calculator')
print('-----')

# building a simple calculator
def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    if b!=0: # avoid being divided by 0
        return round((a/b),2)
    else:
        print('Error! division by zero')
def percentage(a,b):
    return round(((a/b) * 100),2)
def square_root(a,b):
    return a ** b

# loop for user to perform calculation more than one time

while True:
    # get input from user
    num1 = int(input('Enter the first number: '))
    num2 = int(input('Enter the second number: '))

    # operation setting
    operation = input("Enter the operator ('+', '-', '*', '/', '%', 'sqrt'): ")

    # perform calculation based on operation

    if operation == '+':
        print('The result is:', add(num1, num2))
    elif operation == '-':
        print('The result is:', subtract(num1, num2))
    elif operation == '*':
        print('The result is:', multiply(num1, num2))
    elif operation == '/':
        print('The result is:', divide(num1, num2))
    elif operation == '%':
        print('The result is:', percentage(num1, num2))
    elif operation == 'sqrt':
        print('The result is:', square_root(num1, num2))
    else:
        print('Invalid operation, please try again!')
    
    # ask the user if they want perform another calculation
    repeat = input('Do you want to perform another calculation?(yes/no): ').lower()
    if repeat != 'yes':
        print('Thank you for using the python calculator. Goodbye!')
        break

print('-----')

