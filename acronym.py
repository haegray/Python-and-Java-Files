#insert phrase
#for every word in the phrase:
#separate into strings by dividing by space
#print first character of those strings and capitalize them

def acronym():
    phrase = input("Please enter a phrase you would like the acronym for:" )
    words = phrase.split(" ")
    for i in words:
        print(i[0].upper())
    

acronym()

    
        
