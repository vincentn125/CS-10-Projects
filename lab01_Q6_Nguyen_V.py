# Vincent Nguyen
# 1320229

# Lab 1 Question 6
# This program asks the user how many cookies he or she wants to make, 
# then displays the number of cups of each
# ingredient needed for the specified number of cookies.

# 1 batch of cookies is 48 cookies
# 1.5 cups of sugar
# 1 cup of butter
# 2.75 cups of flour

sugarAmount = (1.5/48)
butterAmount = (1.0/48)
flourAmount = (2.75/48)

numOfCookies = int(input("Enter the number of cookies: "))

sugarRequired = sugarAmount * numOfCookies
butterRequired = (butterAmount * numOfCookies) 
flourRequired = flourAmount * numOfCookies


#print("TEST PRINT")
#print(format(sugarRequired, ',.2f'))
print("To make ", numOfCookies, " cookies, you will need: ")
print(format(sugarRequired, ',.2f'), " cups of sugar")
print(format(butterRequired, ',.2f'), " cups of butter")
print(format(flourRequired, ',.2f'), " cups of flour")

#TEST CASE 1 (given)
# Enter the number of cookies: 56
# To make  56  cookies, you will need: 
# 1.75  cups of sugar
# 1.17  cups of butter
# 3.21  cups of flour

#TEST CASE 2
# Enter the number of cookies: 100
# To make  100  cookies, you will need: 
# 3.12  cups of sugar
# 2.08  cups of butter
# 5.73  cups of flour

# TEST CASE 3
# Enter the number of cookies: 67
# To make  67  cookies, you will need: 
# 2.09  cups of sugar
# 1.40  cups of butter
# 3.84  cups of flour

# TEST CASE 4
# Enter the number of cookies: 91
# To make  91  cookies, you will need: 
# 2.84  cups of sugar
# 1.90  cups of butter
# 5.21  cups of flour