###
# 3.1
#
company = "ABC Data"
phone = "555-123-009"
employees = 25
remote_work = True
big_company = employees > 100
income = 4500000
income_per_person = income / employees

print("Variable `company` has value: ", company)
print("and is", type(company))
print("Variable `phone` has value: ", phone)
print("and is", type(phone))
print("Variable `employees` has value: ", employees)
print("and is", type(employees))
print("Variable `remote_work` has value: ", remote_work)
print("and is", type(remote_work))
print("Variable `big_company` has value: ", big_company)
print("and is", type(big_company))
print("Variable `income` has value: ", income)
print("and is", type(income))
print("Variable `income_per_person` has value: ", income_per_person)
print("and is", type(income_per_person))


###
# 3.2
# A program that calculates the sum of two numbers.
# Modify the program to calculate the sum of three numbers.
#
number1 = 71
number2 = 14
number3 = 25
result = number1 + number2 + number3
print('Number 1: ', number1)
print('Number 2: ', number2)
print('Number 3: ', number3)
print('The result of summation: ', result)


###
# 3.3
# A program for swapping two varable values
#
x = 7
y = 34
z = 0 # additional, auxiliary variable
print("Before swapping: x=", x, "y=", y)

# swap the values
z = x
x = y
y = z

print("After swapping: x=", x, "y=", y)


###
# 3.4
# A program that, for a given speed in km/h,
# prints the speed in m/s
speed_kmh = 70
speed_ms = speed_kmh * 1000 / 3600
print(speed_kmh, "km/h = ", speed_ms, "m/s")

###
# 3.5
# A program that calculates the length of the diagonal
# of a rectangle with sides a and b.
#
import math
a = 5
b = 8
diagonal = math.sqrt(a**2 + b**2)
print("We have rectangle with sides ", a, " and ", b)
print("Diagonal is ", diagonal)


###
# 3.6
# Program that calculates the distance 
# to the horizon from a height given
import math

height = input("Enter your height in m: ")
height = float(height)
d = 3.57 * math.sqrt(height)
print("Distance you see on a beach is: ", d, "km")
height = height + 20
d = 3.57 * math.sqrt(height)
print("Distance you see from hotel is: ", d, "km")


###
# 3.7
# A program that calculates and prints:
# - the number of people and percentage of the total
#   population living in the Northern Hemisphere
# - the number of people and percentage of the total
#   population living in the Southern Hemisphere
#
total = 8000000000
north = 7200000000
south = total - north
print("World population: ", total)
print("Northern Hemisphere: ", north)
print("Northern Hemisphere in %: ", north/total*100)
print("Southern Hemisphere: ", south)
print("Nouthern Hemisphere in %: ", south/total*100)


###
# 3.8
# A program that calculates and prints
# the average grade of a student
#
math = 5
art = 4
music = 5
history = 3
average = (math + art + music + history) / 4
print("Average grade is", average)


###
# 4.1
# Printing student's personal data
#
name = "Adam"
age = 24
height = 180
future_age = age + 6
print(f"My name is {name}.")
print(f"I am {age} years old, and my height is {height} cm.")
print(f"In 6 years I will be {future_age} years old.  ")


###
# 4.2
# Write a program that calculates and prints
# the income of a family per person. To print the results
# in a readable form, use f-strings.
#
father_income = 5450
mother_income = 4920
family_members = 5
total_income = father_income + mother_income
income_per_person = total_income / family_members
print(f'Total family income is {total_income}, and income per person is {income_per_person}')


###
# 4.3
#
a = 3
b = 5
print(f'{a}+{b}={a+b}')
print(f'{a}-{b}={a-b}')
print(f'{a}*{b}={a*b}')
print(f'{a}/{b}={a/b}')


###
# 5.1
# A program that reads your first and last name from the keyboard.
# Store this data in two separate variables.
# Then, print your full name i.e. first and last name separated by a single space.
#
first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')
full_name = first_name + ' ' + last_name
print(f'Your first name is {first_name} and your last name is {last_name}')
print(f'And your full name is {full_name}')


###
# 5.2
# A program to calculate the volume and surface area of ​​a cube.
# 
cube_side_string = input('Enter cube side: ')
cube_side = int(cube_side_string)
cube_volume = cube_side**3
cube_surface_area = cube_side**2 * 6
print(f'The volume of a cube with side {cube_side} is {cube_volume}')
print(f'The surface area of a cube with side {cube_side} is {cube_surface_area}')


###
# 5.3
# A program to calculate the volume and surface area of ​​a cuboid.
# 
string_a = input('Enter cuboid side a: ')
a = int(string_a)
string_b = input('Enter cuboid side b: ')
b = int(string_b)
string_c = input('Enter cuboid side c: ')
c = int(string_c)
cuboid_volume = a *b *c
cuboid_surface_area = a*b*2 + a*c*2 + b*c*2
print(f'The volume of a cuboid with sides {a}, {b}, {c} is {cuboid_volume}')
print(f'The surface area of a cuboid with sides {a}, {b}, {c}  is {cuboid_surface_area}')
