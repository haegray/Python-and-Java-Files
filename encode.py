def encode(clearString, key):
    newString = ''
    for aChar in clearString:
        newChar=chr((ord(aChar)+key)%128)
        codedNum=newChar
        codedChar=chr(codedNum)
        codedMsg.append(codedChar)
        codedStr += codedChar
    return(codedStr)

def decode(codedStr, key):
    return(encode(codedStr, 128-key)

def encodeFile(fileName, key):
    file = open(fileName, 'r')
    fileString = encode(file.read(), key)
    return(fileString)

           
  
