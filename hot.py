print('Kill Emotion')
print('-----')

# Display a message for three times
# EXPECTION: don't use print statement three times use FOR LOOP

# Define the number of iteration
for i in range(3):
    # Statement that gets repeated
    print('Kill Emotion')
# Ending the loop with another statement
print('-----')

# Display a countdown from 1-10 using FOR LOOP

# iterating the countdown starting from 1-10
for num in range(10):
    print(num + 1)
# Ending the loop
print('-----')

# Display a message to sell tickets for an event to 20 persons but the system stops when it reaches 0
# EXPECTION: The system don't know how many iterations to perform but must stop when the tickets reaches 0

# Using the while loop to sell the tickets
tickets = int(input('Tickets available: ')) #inital number of available tickets

# avaiable tickets
while tickets > 0: 
    print('Sell ticket') #ticket sold
    tickets = tickets - 1 #number of tickets update
# ending the loop
print('-----')

# Display a countdown from 1 - 10 using while loop

num = int(input('Enter the number: '))

while num <= 10:
    print(f'{num}')
    num = num + 1
# ending the loop
print('-----')

# Create a timer program that will take the number of seconds as input, and countdown to 0
# EXPECTION: Timer should count from 10 - 0

timer = int(input('Enter how many secs.: '))

# system countdown from 10-0
while timer >= 0:
    print(f'{timer}')
    timer = timer - 1
# ending the loop
print('-----')

# Checking boolean with for loop
for i in range(3):
    print(i < 1)
# ending the loop
print('-----')

# Exploring comparison operators
print(5 == 5) # is 5 equal to 5?
print(5 == 7) # is 5 equal to 7?
print(5 != 7) # is 5 different from 7?
print(5 != 5) # is 5 different from 5?
print(5 <= 5) # is 5 less than or equal to 5?
print(5 >= 5) # is 5 greater than or equal to 5?
print('-----')


# Creating a system that grants access to a user when the passwords matches the system password
password = 'secretword'
guess = input('password: ')

# The system keeps asking the user for password till it matches the correct password
while guess != password:
    guess = input('password: ')
# the user gets acesss when it is correct
print('Access Granted')
print('-----')

# A robot display task completed once all labels have been printed
for box in range(20):
    print('Package A')
# Robot ends the loop
print('Task Completed')
print('-----')