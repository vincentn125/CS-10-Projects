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
print("Amount paid for the stock:          $", format(stock1AmountPaid, '13,.2f'))
print("Commission paid on the purchase:    $", format(stock1CommBuy, '13,.2f'))
print("Amount the stock sold for:          $", format(stock1SoldFor, '13,.2f'))
print("Commission paid on the sale:        $", format(stock1CommSell, '13,.2f'))
print("Profit (or loss if negative):       $", format(stock1ProfOrLoss, '13,.2f'))
print("")
print("------------------------------------------------------------")
