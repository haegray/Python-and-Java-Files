def rMax(listofNums):
    if len(listofNums) == 1:
        return listofNums[0]
    else:
        m = rMax(listofNums[1:])
        return m if m > listofNums[0] else listofNums[0]

def main():
    listofNums = eval(raw_input(" Please enter a list of numbers: "))
    print("The largest number is: ", rMax(listofNums))

main()
