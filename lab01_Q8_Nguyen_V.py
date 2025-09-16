# Student Name: Vincent Nguyen
# ID: 1320229

# Lab 1, Question 8
# Program calculate the gravitational force (F)
# and acceleration due to gravity (g) caused by gravitational force exerted by the Earth

# constants
G = 6.67300 * (10**-11)
earthRadius = 6378 * (10.0**3)
m1 = 5.9742 * (10**24)

# input
userMassKG = float(input("Enter a mass in kg: "))

# calculations/processing
gResult = ((((G * m1 * userMassKG))/(earthRadius ** 2)) / (userMassKG))

# output
print("The resulting value of g is", format(gResult, ',.4f'), "which is close to the earth's gravitational force")

## Test case 1
## Enter a mass in kg: 30
## The resulting value of g is 9.8001 which is close to the earth's gravitational force

