#sumList.py
def sumList():
    listOfNumbers=input("Please insert a list of numbers separated by commas:")
    listOfNumbers= listOfNumbers.split(',')
    numList= [float(s) for s in listOfNumbers]
    numList=sum(numList)
    print (numList)
sumList()
    
