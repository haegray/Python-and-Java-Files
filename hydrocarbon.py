#hydrocarbon.py
# A program to calculate the molecular weight of a hydrocarbon.

def main ():
    print("This program determines the molecular weight of a hydrocarbon in grams per mole.")
    print ("First we will define the number of atoms in the molecule.")
    print()
    hmw = 1.0089
    cmw = 12.011
    omw = 25.9994
    print("Please enter the number of atoms of hydrogen, carbon, and oxygen.")
    hydrogen = eval(input("Hydrogen: "))
    carbon = eval(input( "Carbon: "))
    oxygen = eval(input("Oxygen: "))

    if oxygen>0:
        print("Hydrocarbons do not contain Oxygen atoms.")
    else:
        ans = (hmw*hydrogen) + (cmw*carbon)
        print("The molecular weight of the hydrocarbon is ", ans)

main()
    
