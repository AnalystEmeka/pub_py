print('Be Consistent')
print('-----')

# list on py
# list stores mutiple values in a variable and it is mutable
# strings are immutable and they are ordered sequentially

# storing items into a shopping_cart 
shopping_cart = ['laptop',
                 'smartphone',
                 'headphone',
                 'backpack']
# display the list
print(shopping_cart)
print('-----')

# using indexing to call items in a list
# checking for last call from the list

last_calls = ['mom', 'dave', 'lawyer']
# display who called last using indexing 
print(last_calls[0])
print(last_calls[1])
print(last_calls[2])
print('-----')

# storing a list into another variable
animals = ['cat', 'dog', 'bird']
# reassigning
my_pet = animals[1]
# display the new variable 
print(my_pet)
print('-----')

# changing items in a list which means that list are mutable
info = [23, 'John', 'Lagos']
# changing the values in a list
info[0] = 25
info[1] = 'Ada'
info[2] = 'Abia'
# displaying the new variable
print(info)
print('-----')

# displaying list using indexing and concatentate

words = ['rise', 'sun', 'glasses']
# displaying items in the list
print(words[0])
print(words[1])
print(words[2])
# displaying concatentate with list
print(words[1] + words[2])
print('-----')

# A game machine has 5 games installed on it, represented in the list
games = ['soccer', 'tic tac toe', 'snakes', 'puzzle', 'rally']
# EXPECTION: Display the game choosed by user

# instlled games
games = ['soccer', 'tic tac toe', 'snakes', 'puzzle', 'rally']
# user choice
user_choice = int(input('Choose games 0-4: '))
# display user's choice
message = 'Process game:'
print(message + games[user_choice])
print('-----')

# creating a list from values stored in a variable 
name = 'Eben'
age = 5
country = 'Nigeria'
# creating a list with the above variables
info = [name, age, country]
# display the list
print(info[0])
print(info[1])
print(info[2])
print('-----')

# indexing with strings
pet = 'Cat'
# displaying the strings letter
print(pet[0])
print(pet[1])
print(pet[2])
print('-----')

# # string are immutable
# words = 'car'
# words[2] = 't'
# # display the string 
# print('words')

# list are mutable
words = ['car', 'dog', 'bird']
# changing the first item in the list
words[0] = 'cat'
# displaying the new item in the list
print(words)
print('-----')

# using concatenation to get the word 'dog'
d = 'dialogue'
# using concatenate
print(d[0] + d[4] + d[5])
print('-----')

# list slicing to get a portion of list
animals = ['cat', 'dog', 'bird', 'cow']
# using slicing
print(animals[0:1]) # displaying only the first item in the list
print(animals[0:2]) # displaying the first two items in the list
print(animals[1:3]) # displaying the 2nd and 3rd items in the list
print(animals[0:4]) # displaying every item in the list
print('-----')

# slicing can be used on strings
color = 'pink'
# using slicing to get the word 'ink'
print(color[1:4]) # displaying the word 'ink'
print(color[:]) # displaying the color 'pink'
print('-----')

# In a race competition, there are 6 participants listed
# EXPECTION: group the players into three groups having two players each and display eaach groups

# race players
players = ['Alice', 'Bob', 'Charles', 'David', 'Eve', 'Frank']

# create the group using slicing
# create first group
g1 = players[0:2]
# create second group
g2 = players[2:4]
# create third group
g3 = players[4:6]

# displaying each groups created
print('Group 1: ')
# displaying the first group
print(g1)

print('Group 2: ')
# displaying the second group
print(g2)

print('Group 2: ')
# displaying the third group
print(g3)
print('-----')

# slicing omitting the start, to slice from the very first element
cart = ['lamp', 'candle', 'chair', 'carpet']
# displaying the slicing
print(cart[:3]) # displaying the first three items in the list
print('-----')

# slicing omitting the stop, to slice until the very last element
cart = ['lamp', 'candle', 'chair', 'carpet']
# displaying the slicing
print(cart[1:]) # displaying the last three items in the list
print('-----')

# slicing omitting the start and stop
print(cart[:]) # displaying everything in the list
print('-----')

# indexing from the end is called negative indexing 
animals = ['cat', 'dog', 'bird', 'cow']
# displaying the negative slicing
print(animals[-1]) # displaying the last item in the list
print(animals[-2]) # displaying the second to last item in the list
print(animals[-3:]) # displaying the last three items in the list
print(animals[:-1]) # displaying the first three items in the list
print(animals[::-1]) # displaying the reversed items in the list
print(animals[-3:-1]) # displaying the 2nd and third item in the list
print('-----')

# combinig postive with negative index
print(animals[1:-2]) # displaying only the second item in the list
print(animals[1:-1]) # displaying the 2nd and third item in the list

