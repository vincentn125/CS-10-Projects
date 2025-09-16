# Student Name: Vincent Nguyen
# ID: 1320229

# Lab 1, Question 7
# Program prompts user to enter a four-digit integer 
# and displays the number in reverse order

# input/data
userNumber = int(input("Enter an integer: "))

# Calculations/Processing
firstNumber = (userNumber % 10)
secondNumber = (userNumber // 10) % 10
thirdNumber = (userNumber // 100) % 10
fourthNumber = (userNumber // 1000)

#output 
print(firstNumber)
print(secondNumber)
print(thirdNumber)
print(fourthNumber)


##Test run 1
##Enter an integer: 3125
##5
##2
##1
##3
##
##Test run 2
##Enter an integer: 1024
##4
##2
##0
##1
##
##Test run 3
##Enter an integer: 1983
##3
##8
##9
##1
