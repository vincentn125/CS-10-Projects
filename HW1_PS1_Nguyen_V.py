# Student Name: Vincent Nguyen
# ID: 1320229
# Homework 1, Program Set 1

# Program tracks and reports 3 stocks on its costs and profit or loss

# input for stock 1
print("*********************************")
print("* Enter Information for Stock 1 *")
print("*********************************")
stock1Name = input("Enter Stock Name in Uppercase: ")
stock1NumOfShares = float(input("Enter Number of Shares  :  "))
stock1BuyPrice = float(input("Enter Purchase Price  :  "))
stock1SellPrice = float(input("Enter Selling Price  :  "))
stock1Comm = float(input("Enter Commission (in percent) :  "))

# calculations on stock 1
stock1AmountPaid = (stock1NumOfShares * stock1BuyPrice)
stock1CommFloat = (stock1Comm / 100)
stock1CommBuy = (stock1AmountPaid * stock1CommFloat)
stock1SoldFor = (stock1NumOfShares * stock1SellPrice)
stock1CommSell = (stock1SoldFor * stock1CommFloat)
stock1ProfOrLoss = (stock1SoldFor - stock1CommSell) - (stock1AmountPaid + stock1CommBuy)

# output on stock 1
print("")
print("")
print("------------------------------------------------------------")
print(stock1Name)
print("")
print("Amount paid for the stock:          ${:13,.2f}".format(stock1AmountPaid))
print("Commission paid on the purchase:    ${:13,.2f}".format(stock1CommBuy))
print("Amount the stock sold for:          ${:13,.2f}".format(stock1SoldFor))
print("Commission paid on the sale:        ${:13,.2f}".format(stock1CommSell))
print("Profit (or loss if negative):       ${:13,.2f}".format(stock1ProfOrLoss))
print("")
print("------------------------------------------------------------")
