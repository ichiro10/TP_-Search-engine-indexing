from nltk.tokenize import RegexpTokenizer

import os 


def tok():
    inpath = "/home/ichiro19/Desktop/INFO4/S8/RI/collection/"
    outpath ="/home/ichiro19/Desktop/INFO4/S8/RI/collection_tokens/"
    for filename in os.listdir(inpath) :
       #print(filename)
       fich = open(inpath + filename, "r")
       fich_tok = open(outpath + filename + ".tok", "w")
       for line in fich :
          #print(line.strip())
          tokenizer = RegexpTokenizer('[A-Za-z]\w{1,}') 
          chaine_tok = tokenizer.tokenize(line)
          #print(chaine_tok)
          S=""
          for x in chaine_tok :
             x= x.lower()
             #print(x)
             S=S+" "+x  
          #print(S)   
          fich_tok.write(S+"\n")  
       fich_tok.close()
       fich.close()  
        
tok()       
       

       
       
       

   
