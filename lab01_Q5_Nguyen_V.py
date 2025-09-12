# Vincent Nguyen
# 1320229

# Lab 1 Question 5
# This program aks the user to enter the projected amount of total sales
# then displays the profit that will be
# made from that amount.

# User Input

totalSales = float(input("Enter the projected total sales: "))
profitMargin = 0.24 #24% profit margin

totalProfit = (totalSales * profitMargin)

print("The profit made from this amount:", format(totalProfit, ',.2f'))

# TEST CASE 1
'''
Enter the projected total sales: 1250.00
The profit made from this amount: 300.00
'''

# TEST CASE 2
'''
Enter the projected total sales: 1000
The profit made from this amount: 240.00

'''

# TEST CASE 3
'''
Enter the projected total sales: 8950.23
The profit made from this amount: 2,148.06

'''
