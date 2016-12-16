#sumStrings.py
def sumStrings(strList):
    toNumbers=[]
    sum = 0
    for i in strList:
        num = eval(i)
        toNumbers.append(num)
    for num in toNumbers:
        sum = sum + num
    print(sum)
sumStrings()
