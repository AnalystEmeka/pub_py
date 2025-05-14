print('rule the world')
print('-----')

# Developing a Finance app to help user grow savings
# EXPECTION: Take the savings and calculate the end amount 
savings = float(input('Enter the Amount: '))

# savings grow after 1 year at a 5% annual interest rate
balance = round(savings * 1.05, 2)

# converting the balance into a string and updating the variable
balance = str(balance)

# concatenate the 2 strings to produce a message
message = 'Amount in 1 year: ' + f'${balance}'

# Display the message
print(message)
print('-----')


# A video game wants to check the players that would move to the next level
# EXPECTION: Display True if score is greater than 100 and False otherwise

# The program takes the score of as an input
score = int(input('score of the player: '))

# Checking if the players will move to the next level
next_level = score > 100
next_level = str(next_level)
result = 'Proceed to the next level: ' + next_level

# display the players chance to next level
print(result)
print('-----')


# Smartwatch checks the heart rate of the user
# EXPECTION: Display the heart rate of user

heart_rate = int(input('Enter heart rate: '))

# checking if the heart rate is normal
normal = heart_rate >= 60
normal = str(normal)
level = 'The heart_rate is normal: ' + normal

# display the user heart_rate
print(level)
print('-----')


# Let the temperature system turn on the AC if the temp. is greater than 30 °C

temp = int(input('temp is: '))

# checking the room temperature
ac_on = temp > 30
ac_on = str(ac_on)
turn_on = 'switch_on the AC: ' + ac_on

#display the output
print(turn_on)
print('-----')



# Develop a system fitness checker to check if daily goals are completed
# EXPECTION: Display True if the daily goals is achieved and False otherwise

# Goals reqired to be achieved, steps count more than 10000 
# or required time more than 30 minutes
steps = int(input('Enter steps count: '))
active_minutes = int(input('Enter min. covered: '))

# checking if the user achived the goal from the result collected
goal_achieved = steps > 10000 or active_minutes > 30

# Display the result
print(goal_achieved)
print('-----')


# Checking data type of a value in a variable
temp = 24
unit = '°C'

# Display the data type 
print(type(temp))
print(type(unit))
print(str(temp) + unit)
print('-----')


# Checking the keys or coin a player collected in video game to moves to the next level
coins = int(input('coins collected: '))
keys = int(input('keys collected: '))

# Display if the player moves to the next level
move_forward = coins > 30 or keys > 1
move_forward = str(move_forward)
proceed = 'proceed to next level: ' + move_forward

# Display the players result
print(proceed)
print('-----')


