print('Be Focused')
print('-----')

# print() functions accept arguments of any data type
print('Online:', True) # string and boolean
print('Credit:', f'${395.91}') # string and float
print(2, 'bananas') # integer and strings
print('-----')

# print() can accept math, logical and comparison operations
print(55 * 3) # maths
print(5 > 7)  # comparison
print(True and False) # logical
print('motor' + 'bike') # concatenation
print('-----')

# variable as argument
balance = 304
print('money in the account:', f'${balance}')
print('-----')

# A function as argument for another function
print(type('words')) #type('words') is an argument of print()
print('-----')

print(range(3)) #range(3) is an argument of print() and display of sequence of 3 numbers
print('-----')

# upper and lower() functions for strings to be used to  change to uppercase and lowercase respectively
print('SmarTPhone'.lower()) # change to lowercase
print('SmarTPhone'.upper()) # change to uppercase

# changing a variable to a upper() or lower() 
brand = 'uber'
print(brand.upper())  # changing the argument to uppercase
print('-----')

# using capitalize() to change first letter to uppercase and the rest to lowercase
print(brand.capitalize()) # capitalize the variable
print('-----')

# strings are immutable and functions can't change it.

item = 'smartwatch'
print(item.upper())
print(item) # original string
item2 = item.upper() # storing the modified string in a variable to keep it
print(item2)
print('-----')

# using find() function to check if a character or a pattern of characters is present in a string
print('bee'.find('e')) # if the character is present multiple times, it returns the first occurence (lower index)
print('-----')

print('robot'.find('r')) # it returns the exact index og the character of a string
print('-----')

print('robot'.find('a')) # if the character is not found in the string, it retrurns negative index -1
print('-----')

# Analyze data from a survey and convert specific pieces of text data to uppercase
# EXPECTION: The text data as input then convert to uppercase and display
user = input('What is your name: ') # text data
# convert to uppercase
user = user.upper()
# display
print(user)
print('-----')

# len() function stands for length
# it is used to return the number of item in a list or string, counts from 1
movies = ['Avatar', 'Titanic', 'Avengers']
print(len(movies))
print('-----')

# using len() on a string 
watching = 'Avatar'
print(len(watching)) # counts from 1 (total_char: 6)
print('-----')

# append() function adds a new item to the end of a list
# it called using dot notation because its specific to list

songs = ['Yesterday', 'Hello', 'Believer']
songs.append('Imagine') # appears as the last item in the list
# display
print(songs)
print('-----')

movies = ['Avatar', 'Titanic', 'Avengers']
movies.append('Snowfall')
# display
print(movies[3])
print('-----')

# insert() function is used to add item in a list at a specific position
item = ['pen', 'eraser', 'pencil']
item.insert(1, 'marker') # add as the second value in the list
# display
print(item)
print(item[1])
print('-----')

# combining append() and insert()
colors = ['red', 'blue', 'green']
colors.insert(2, 'yellow') # added as the third item in the list
colors.append('black') # added as the last item in the list
# display 
print(colors[2])
print(colors)
print('-----')

# pop() function removes an element from a list, the position of the item to be refused in the list must be specified
items = ['book', 'pen', 'pencil']
items.pop(1)
# display
print(items)
print(item[1])
print('-----') 

points = [25, 50, 70, 75, 100]
points.pop(2) # removed the third item in the list
points.append(125) # added as the last item in the list
# display
print(points)
print('-----')

cars = ['BMW', 'Toyota', 'Audi', 'Honda']
cars.pop(1) # removed the second item in the list
cars.insert(2, 'Telsa') # added as the third item in the list 
# display
print(cars)
print('-----')

# def() is used to call a function as many times as you need
# function definition
def greet():
    print('Hello mate')
    print('Lock in MF')
# function call
greet()
print('-----')

# A function might require arguments to complete its tasks

# function definition
def personal_greet(name):
    print('Hello', name)
    print('Rule the world')
# function call
personal_greet('Emeka')
print('-----')
personal_greet('John')
print('-----')

# A function makes blocks code easy to execute

# function definition
def double(num):
    print(num*2)
# function call
double(6) # calling the argument num(6) to be multipled by 2
print('-----')

# function definition
def bmi(weight,height): # taking two arguments for bmi
    index = round(weight/(height * height), 2) # define the index
    print(index) # displays the body mass index
# function call
bmi(50,1.5) # the weight and height of the bmi to get the index result
print('-----')

# using the return function

# defining function
def bmi(weight,height):
    index = weight/(height * height)
    return index # sends the return values back
# calling the function and using return value
patient_1 = bmi(61, 1.83) # stores return value
print('Underweight:', patient_1 < 18.5)
print('-----')

# Another calls
patient_2 = bmi(75, 1.74)
print('Underweight:', patient_2 < 18.5)
print('-----')

# Calculate the shipping cost for customer orders based on weight of the package
# The cost per kilogram is $5
# EXPECTION: Calculate and display it from user input

# taking the package weight
package_weight = int(input('Enter the weight: '))

# defining function to calculate the package weight
def shipping_cost(package_weight):
    package = package_weight * 5 # getting the package weight
    print('The package weight is:', package)
# function call
shipping_cost(package_weight)
print('-----')

# convert a distance in miles to kilometers
def convert_km(miles):
    kilometers = round((miles * 1.61), 2)
    return kilometers
# function call
distance = convert_km(200)
print(distance)
print('-----')

# checking the length and width of an object
def rect(length,width):
    area = length * width
    perimeter = 2*length + 2*width
    return area, perimeter # returning the values
# function call
x,y = rect(50,100) # return the values of area and perimeter
print(f"area:{x}\nperimeter:{y}")
print('-----')

# getting the price of the land
def land(d1,d2):
    area = d1 * d2
    perimeter = 2*d1 + 2*d2
    price = 1000 * area
    return area, perimeter, price
# function call
x,y,z = land(90, 180)
print(f"area:{x}\nperimeter:{y}\nprice:${z}")
print('-----')

# checking if we made profit from our investment 
def profit(d1,d2):
    area = d1 * d2
    invest = area > 700
    return invest
# function call
buy = profit(80, 160)
print(f'profitable:{buy}')
print('-----')

# when a code in a function ends when a value is returned
# any other additional lines of codes after the return line will be ignored

def rect(d1,d2):
    area = 0
    return area 
    # end of function execution
    area = d1 * d2 # not executed
x = rect(50,100)
print(x)
print('-----')

# A function can be given a default argument if a function is called without an argument
def greet(name = 'Guest'):
    print('Welcome', name)
# function call
greet() # default argument
greet('James')
print('-----')

# Getting for a customer below 18 and a student
# customer price
price = 100
discount = 100 * (1 - 20/100)
def reduction(age, student):
    if age < 18 or student == 'yes':
        return f'20% discount: ${discount}'
    else:
        return f'No discount: ${price}'
# function call
customer = reduction(int(input('Enter your age: ')), 
                     input('Are you a student: ').lower()) 
print(customer)
print('-----')

# getting an income and tax rate of employee
income = int(input('Enter your income: '))
rate = int(input('Enter tax_rate: '))
def tax(income, rate):
    tax_rate = round((income * rate/100), 2)
    return tax_rate
# function call
employee = tax(income, rate)
print(f'your tax deduction: ${employee}')
print('-----')

# create a program to add and multiply two numbers
# EXPECTION: create two function add() and multiply()
# --- They should compute the result and return them
# --- The result should be printed from outside the function

# defining function
def add(a,b):
    addition = a + b
    return addition
def multiply(a,b):
    multiplication = a * b
    return a * b
# function call
a = int(input('enter number a: '))
b = int(input('enter number b: '))
print('-----')
print(f"addition:{add(a,b)}\nmultiplication:{multiply(a,b)}")
print('-----')


