#cashregister.py

#This program is designed to calculate and display sales price which is
#list price plus a 5.3% sales tax.

def cashregister():
    print("Please input the list price of the item you would like to purchase.")
    listPrice=eval(input("price: "))
    salesPrice= (listPrice + (.053 * listPrice))
    print("The total cost is", salesPrice)

cashregister()

#IOP:
#Please input the list price of the item you would like to purchase.
#price: 1.50
#The total cost is 1.5795
#>>> ================================ RESTART ================================
#>> 
#Please input the list price of the item you would like to purchase.
#price: .99
#The total cost is 1.04247
