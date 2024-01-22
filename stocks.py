#stocks program
comm_percentage_stock_purchase = float(input("Enter commission rate percentage (ex 0.03) on stock purchase: "))
comm_percentage_stock_sale = float(input("Enter commission rate percentage (ex 0.03) on stock sale: "))
shares_purchased = int(input("Enter number of shares purchased: "))
shares_sold = int(input("Enter number of shares sold: "))
purchase_price = float(input("Enter purchase price per share: "))
sell_price = float(input("Enter sell price per share: "))
#calculations:
amountPaidForStock = shares_purchased * purchase_price
purchaseCommission = comm_percentage_stock_purchase * amountPaidForStock
# Part A
totalPaid = amountPaidForStock + purchaseCommission
stockSoldFor = shares_sold * sell_price
sellingCommission = comm_percentage_stock_sale * stockSoldFor
totalReceived = stockSoldFor - sellingCommission
profitOrLoss = totalReceived - totalPaid
# Part b
#print("Amount paid for stock: $", format(amountPaidForStock, '.2f'))
print("Amount paid for stock: $" + '{:,.2f}'.format(amountPaidForStock))
print("Commission paid on the purchase: $" + '{:,.2f}'.format(purchaseCommission))
print("Amount the stocks sold for: $" + '{:,.2f}'.format(stockSoldFor))
print("Commission paid on the sale: $" + '{:,.2f}'.format(sellingCommission))
print("Profit (or loss if negative): $" + '{:,.2f}'.format(profitOrLoss))
