def wordcount():
    paper = input("Please copy and paste your writing here." )
    words=paper.split(" ")
    print("The number of words are: " + str(len(words)))

wordcount()
