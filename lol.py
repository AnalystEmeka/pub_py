print('Stay Wicked')
print('-----')

# Create a system that gives discount to customers according age
# EXPECTION: under 18 gets a discount but above 18 pays regular price using IF-ELSE STATEMENT

# sets the value of age
age = int(input("what's your age: "))
if age >= 18:
    # executed only if customer's age is above or 18
    print('Regular price')
else:
    # executed only if age is less than 18
    print('Discount')
# end the loop
print('Proceed to payment')
print('-----')

# The machine gives discount to students or under 18

# sets the value of age and student
age = int(input("What's your age: "))
is_student = input('Are you a student (yes/no): ').lower()

if age < 18 or is_student == 'yes':
    # executed if only student or under 18
    print('Discount')
else:
    # executed if not student or above 18
    print('Regular price')
# end the loop
print('Proceed to payment')
print('-----')

# A smart parking lots display different messages to visitor based on the available spaces
# EXPECTION: Inform the user about available spaces in the parking lot

# generating available parking lot
spaces = int(input('Available space: '))

# Display message if spaces are available
if spaces > 0:
    print('Park your car')
# Display a different message if spaces are not available
else:
    print('Sorry, the parking lot is full')
# ending the loop
print('-----')

# Design a health care system that tells the patient when they have high temp.
# take the body temperature of the patient

body_temp = int(input('Body temperature: '))

# setting different temp range 
if body_temp <= 35:
    # display message if patient tempm is below 35°C
    print('Low temperature: Visit your doctor')
elif body_temp > 37:
    # display message if patient temp is above 37°C
    print('High temperature: Visit your doctor')
else:
    # display message if patient temp is not above 37°C
    print('Normal body temperature')
# end the loop
print('-----')

# The discount only applies to distinct customers below age 18
age = int(input("what's your age: "))
if age < 18:
    print('Apply discount')
print('Proceed to payment')
# ending the loop
print('-----')

# Design a discount system using NEST STATEMENT

# sets value of age and student
age = int(input("what's your age: "))
is_student = input('Are you a student (yes/no)? ').lower()

# display if age is less than 18
if age < 18:
    # display if under 18 and also a student
    if is_student == 'yes':
        print("20% discount")
    else: 
        # execute if under 18 and not a student
        print("10% discount")
else:
    # execute if customer 18 or over
    print('Regular price')
# end the loop
print('proceed to payment')
print('-----')

# Develop a software for medical device that informs patients about their blood sugar level
# EXPECTION: Display different messages to the patients based on their blood sugar level

# Glucose level is collected by software
glucose_level = int(input('Enter blood sugar level: '))

# display message if glucose level is less than 70
if glucose_level < 70:
    print('Low glucose level')
# display message if glucose level is greater than 140 
elif glucose_level >= 140:
    print('High glucose level')
# display message if none of conditions above are met
else:
    print('Normal glucose level')
# end the loop
print('-----')