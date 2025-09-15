# Student Name: Vincent Nguyen
# ID: 1320229

# Lab 1, Question 4
# This program reads user input of radius and length of a cylinder
# then calculates the area of one base
# and volume of a cylinder 

# input/data
radiusCylinder = float(input("Enter the radius of a cylinder: "))
lengthCylinder = float(input("Enter the length of a cylinder: "))

# calculations/processing
baseArea = (radiusCylinder * radiusCylinder) * 3.141
volume = (baseArea * lengthCylinder)

#output
print("The base area is", baseArea)
print("The volume is", volume)

## Test run 1
##Enter the radius of a cylinder: 5.5
##Enter the length of a cylinder: 12
##The base area is 95.01525
##The volume is 1140.183

##Test run 2
## Enter the radius of a cylinder: 6
##Enter the length of a cylinder: 7
##The base area is 113.076
##The volume is 791.5319999999999

## Test run 3
##Enter the radius of a cylinder: 4
##Enter the length of a cylinder: 21
##The base area is 50.256
##The volume is 1055.376
