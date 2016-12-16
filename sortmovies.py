def censor(Susan):
   infile = open(Susan,"r")
   outfile = open("censored.txt","w")
   for line in infile:
       text=line.split(" ");
       for word in text:
           word = ''.join(c for c in string if c.isalnum())
           if len(word)==4:
               line=line.replace(word,"****")
       outfile.write(line)
   outfile.close()
   infile.close()
censor()
