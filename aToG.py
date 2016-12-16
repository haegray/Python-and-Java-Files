#aToG.py
def aToG(aChar):
    num = ord(aChar)
    if (num>84):
        newNum = num - 20
    else:
        newNum = num + 6
    newChar=chr(newNum)
    return(newChar)

aToG()
