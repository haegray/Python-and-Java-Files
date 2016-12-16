def main(): 
    phrase = raw_input("Enter a phrase:") 
    words = phrase.split(" ") 
    letters = [i[0].upper() for i in words] 
    print "".join(letters) 
main()
