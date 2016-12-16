# caesar.py
# use chars asciii 0-127    

def encode(clearStr, key):
    codedMsg = []
    codedStr = ''
    for ch in clearStr:
        shiftedNum = ord(ch) 
        keyedShiftedNum = (shiftedNum + key)%(128)
        codedNum = keyedShiftedNum   
        codedChar = chr(codedNum)
        codedMsg.append(codedChar)
        codedStr += codedChar
    return(codedStr)

def decode(codedStr, key):
    return(encode(codedStr, 128-key))

def encodeFile(fileName, key):
    file = open(fileName, 'r')
    fileString = encode(file.read(),key)
    return(fileString)

def decodeFile(fileName, key):
    file = open(fileName, 'r')
    fileString = encode(file.read(),128-key)
    return(fileString)

def encodeToFile(fromFile, toFile, key):
    writeToFile = open(toFile,'w')
    print(encodeFile(fromFile, key), file = writeToFile)
    print('message now encoded in file', toFile)

def decodeFromFile(fromFile, toFile, key):
    writeToFile = open(toFile,'w')
    print(encodeFile(fromFile, -key), file = writeToFile)
    print('message now encoded in file', toFile)
    
    

        
