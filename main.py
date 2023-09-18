# 1.A asking the name
name = input("What is your name?")
# Greets the user by their name
print(f"Hello, {name} ! Nice to meet you.")

#############
 # 2.A  Get the radius of the circle from the user
radius = float(input("Enter the radius of the circle: "))

# To calculate the area ,use the formula , Area = π * r^2
import math
area = math.pi * (radius ** 2)

# Print the calculated area
print(f"The area of the circle with radius {radius} is {area:.2f}")

#############
# 3.A get the length and breadth from the user
length = float(input("Enter the length of the rectangle:  "))
breadth = float(input("Enter the breadth of the rectangle: "))
# using the formula,perimeter= 2*(length+breadth) and using the formula, area = length*breadth

perimeter = 2*(length+breadth)
area = length * breadth
# print the calculated perimeter and area
print(f"The perimeter of the rectangle is {perimeter}")
print(f"The area of the rectangle is {area}")

##############
# 4.A get the value of the three integers from the user
a = float(input("Enter the first integer number: "))
b = float(input("enter the value of the second integer number: "))
c = float(input("enter the value of the third integer number : "))
# solving the sum, product and average of all the integers
sum = a+b+c
product= a*b*c
average = sum/3
# print the calculated sum , product and average
print(f"the sum of the integers is {sum}")
print(f"the product of the integers is {product}")
print(f"the average of the integer is {average}")

################
# 5.A # Conversion
POUNDS_PER_TALENT = 20
LOTS_PER_POUND = 32
GRAMS_PER_LOT = 13.3

# put in the values
talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))

# Calculate the total weight in lots
total_lots = (talents * POUNDS_PER_TALENT + pounds) * LOTS_PER_POUND + lots

# Calculate kilograms and grams
kilograms = int(total_lots // 1000)
grams = total_lots % 1000

# by solving
print(f"The weight in modern units:")
print(f"{kilograms} kilograms and {grams:.2f} grams.")












