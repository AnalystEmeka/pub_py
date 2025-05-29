print("Don't Be Normal")
print('-----')

# storing items in a dictionary
user: dict = {8: 'Obi', 9: [9, 67]}
print(user)
print('-----')

# storing items in a list
name: list = [9, 78, 0, 'O']
print(name)
print('-----')

# stored items in a dictionary is represented by a KEY:VALUE pair
age = {'Dave': 24, 'Mary': 3, 'John': 60}
print(age['Dave']) # getting an item from a dict with a key pair
print(age['John'])
print('-----')

print(age.values()) # getting the values from a dict using values pair
print('-----')

# imaigine working at a car dealership and store the car data in a dictionary
# EXPECTION: The program needs to take the key as input and output the corresponding values

# Details of car stored in the dictionary 
car = {
    'brand': 'BMW',
    'year': 2018,
    'color': 'Black',
    'mileage': 15000
}

# getting the details of the car form key as input
print(car[input('Get the details of the car(brand, year, color, mileage): ')])
print('-----')

# key in a dict. can be checked by using 'in and not in' and you can also do that in a list
# stored items in a dict.
shirt_size = {1: 'Medium',
              2: 'Large',
              3: 'Extra_large'}
# checking if a key is in the shirt_size dict.
print(1 in shirt_size) # the key exist True
print('Large' in shirt_size) # the key is not in the dict. so False
print(4 not in shirt_size) # there is no fourth item in the dict so True
print('-----')

# get() does the same thing as indexing, but if a key is found in a dict. it returns another specified value instead
pairs = {1: 'apple',
         'orange': [2, 3, 4],
         True: False,
         12: 'True',
         }
# using get() and key pair to get an item from a dict.
print(pairs.get('orange')) # get the value of the pair in the dict
print(pairs.get(7,5)) # return the last num in the tuple because not in the dict.
print(pairs.get(1256, 'Not Found')) # return the string in the tuples because not in the dict.
print('-----')

# using get() to sort a dict.
fib = { 1: 1,
       2: 1,
       3: 2,
       4: 3
       }
# display the result
print(fib.get(4,0) + fib.get(7,5)) # get the value of the key found which is key:4 and value:3
                                    # output the value of the key not found which is 5 and sum(5+3) and output is 8
print('-----')

# Tuples are very similar to lists but they are immutable
# It is created using parentheses rather than square brackets
# Tuples can be accessed with their index just like list

words: tuple = ('spam', 'eggs', 'sausages')
# displaying the tuples with index
print(words[0])
print('-----')

# Reassigning a value in a tuple causes an error
# words[1] = 'chesses' # it will result to an error because it is immutable
# print('-----')

# tuples can be created without parentheses
item: tuple = 'book', 'pen', 'pencil'
print(item[1])
print('-----')

# A list is given of contacts, where each contact is respresented by tuple, with the name and age of the contact
# EXPECTION: complete the program to get a string as input, search for the name in the list of contacts 
# output the age of the contact and if the contact is not found, the program should out 'Not Found'

# list and tuples of contact
contacts: list = [('James', 42),
                 ('Amy', 24),
                 ('John', 31),
                 ('Amanda', 63),
                 ('Bob', 18)
                 ]
# collecting the user input and output the contact in the list

name = input('Enter your name: ').capitalize()
found = False

for contact in contacts:
    if contact[0] == name:
        print(name, 'is', contact[1])
        found = True
        break
if not found:
    print('Not Found')
print('-----')

# Tuples unpacking
# Tuples unpacking allows you to assign each item in a collection to a variable

number = (1, 2, 3)
a,b,c = number
# display the tuples
print(a)
print(b)
print(c)
print('-----')

# swap can be performed in tuples unpacking
x,y = [1, 2]
x,y = y,x
# display the result
print(x)
print(y)
print('-----')

# Tuples can be unpacked using asterisk(*)
# When a variable is prefaced with an asterisk(*)
# it takes all values from the collection that are left over from the other variables

a,b,*c,d = [1,2,3,4,5,6,7,8,9]

# display the output
print(a)
print(b)
print(c)  # takes the remain values in the list from 3-8.
print(d)
print('-----')

# Tuples unpacking with asterisk(*)

a,b,c,d,*e,f,g = range(20) # number from 0-19 
print(e) # takes the remaining values in the list after a-d and leaves the last two numbers for f,g
print(len(e)) # counts the remaining number in the list and gives the output
print('-----')

# Sets are similar to list or dictionaries
# They are created using curly braces, and are unordered which means that they can't be indexed
# in operator is used to check whether an item is part of a set

num_set = {1, 2, 3, 4, 5}
# checking if a number is part of the set
print(3 in num_set, ': Found')
print(9 in num_set, ': Not Found')
print('-----')

# using if statement to check an item in a set

letters = {'a', 'b', 'c', 'd'}

# checking to know whether to find 'e'
if 'e' not in letters:
    print(1)
else:
    print(2)
print('-----')

# add() is used to add new items into a set
# remove() is used to delete a specific element from the set
# len() is used count the number of items in the set
# set removes duplictes elements only output unique elements

points = {1, 2, 1, 3, 1, 4, 5, 6}

print(points) # output only unique elements in the set
print(len(points)) # output the number of unique elements in the set
print('-----')
points.add(56) # adds new item in the set
points.remove(1) # removes an item from the set
points.remove(2) # removes an item from the set
print(points) # output the new set created
print(len(points)) # output the number of unique items in the set
print('-----')

letter = {'a', 'b', 'c', 'd'}
letter.add('y')
print(letter)
print(len(letter))
print('-----')

# Mathematical operations can be used to combine sets

# The union operator | combines two sets to form a new one containing items in either
# The intersection operator & gets items only in both set
# The difference operator - gets items in the first set but not in  the second
# The symmetric difference operator ^ gets items in the either set, but not both

point1 = {1, 2, 3, 4, 5, 6, 1.5, 'q'}
point2 = {4, 5, 6, 7, 8, 9, -5}

# using operators to get different outputs from the sets
print(point1 | point2) # Joining the unique values in both sets
print(point1 & point2) # gets only items in both sets
print(point1 - point2) # gets only items in point1 different from point2
print(point2 - point1) # gets only items in point2 diferent from point1
print(point1 ^ point2) # gets items different in both sets
print('-----')

# working on a recuritment platform, which should match the available jobs and the candidate's based on their skills
# the skills required for the job, and the candidate's are stored in sets
# EXPECTION: output the matched skills and join both skills

skills = {'python', 'html', 'sql', 'c++', 'java'}

job_skills = {'html', 'css', 'js', 'c#', 'nodejs'}

matched_skills = (skills & job_skills).pop()
# extract only the matching skills
print(matched_skills)
print('-----')
jobined_skills = (skills | job_skills)
print(job_skills)
print('-----')

# List Comprehension
# List Comprehension is useful to shorten a list or code

# list comprehension
cubes = [i**3 for i in range(5)] # multiples each number by power of 3 until it produces 5 numbers
# display the result
print(cubes)
print('-----')

# list comprehension to output even numbers
num = [i*2 for i in range(1, 11)] # multilples each number by power of 3 until it produces 10 numbers
print(num)
print('-----')

# produces numbers ranging from 5 to 10 and multiplied by 10
nums = [i*10 for i in range(5,11)] 
# display the result
print(nums)
print('-----')

# using if statement in a list comprehension
even = [i**2 for i in range(10) if i**2 %2== 0] # multiply by power of 2 and produce only numbers divisible by 2
#display result
print(even)
print('-----')

# creating list of multiples of 3 from 0 to 20
mul = [num*3 for num in range(21) if num %3==0 ] # produce only numbers divisible by 3
# display result
print(mul)
print('-----')

# Advanced list comprehension

# producing a range of 5 numbers raised by the power of 2
number = [] # creating an empty list

for i in range (1, 6): # starts from numbers 1 - 5
    number.append(2**i) # add 2 raised to the power of i (num: 1-5) into the number list

print(number)
print('-----')

# shorten the above with list comprehension

number = [2**i for i in range(1, 6)] # print numbers 1-5 raised to the power 2 excluding 6
# display result
print(number)
print('-----')

# using math function in list comprehension
# import maths function like sqrt()

import math
# list of numbers in the list
num = [49, 64, 81, 100, 121]
# for n in num: go through each number (n) in the num list 
# if n %2 == 0: only choose the numbers that are even (divisible by 2)
# math.sqrt(n): take the square rrot of those even numbers
new_list = [math.sqrt(n) for n in num if n%2 == 0]
# display the final list of square roots
print(new_list)
print('-----')

# using list comprehension to turn a string into a set

word = 'programming'
# getting the set of the string
alphabet = {x for x in word}
# displaying the set
print(alphabet)
print('-----')

# without list comprehension in dict

numbers = [1, 2, 3, 4, 5]

square_dict = dict()

for num in numbers:
    square_dict[num] = num**2

print(square_dict)
print('-----')

# using list comprehension for the above code
# conveting the number in the list to power of 2 with key:value pair
square_dict = {num:num**2 for num in numbers}
# displaying key:value pair of dict
print(square_dict)
print('-----')

# A store wants to increase the price of items that are greater than $2 by $1.5
# EXPECTION: display old_price and new_price with and without list comprehension

# without list comprehension
# items in the store
old_price = {'milk': 1.02,
             'coffee': 2.3,
             'bread': 2.5
             }
# assigning the new_price to a dict
new_price = dict()

# checking for item above $2 to assign new price
for key, value in old_price.items():
    if value > 2:
        new_price[key] = round((value * 1.5),2)
    else:
        new_price[key] = value
print(new_price)
print('-----')

# with list comprehension for above code
new_price = {key:round((value * 1.5), 2) if value > 2 else value for (key,value) in old_price.items()}
# display new_price
print(new_price)
print('-----')

# A list contains list of names but we want to print names starting with j

names = ['John', 'James', 'Emmy', 'Michael', 'Jimmy']

# collect only names staring with J
J_names = []

for name in names:
    if 'J' in name:
        J_names.append(name)
# display J_names
print(J_names)
print('-----')

# using list comprehension for the above code
J_names = [name for name in names if 'J' in name]
# display J_names
print(J_names)
print('-----')

# making new copy of the list with list comprehension
new_copy = [name for name in names]
# display copy of the list
print(new_copy)
print('-----')

# convert to list comprehension 

animals = ['lion', 'tiger', 'monkey', 'elephant', 'frog']

f_animals = []

for animal in animals:
    f_animals.append(animal.title())

# display f_animals:
print(f_animals)
print('-----')

# converting above code to list comprehension
f_animals = [animal.title() for animal in animals]
# display f_animals
print(f_animals)
print('-----')



