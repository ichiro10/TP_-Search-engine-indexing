import os
def dicos():

   dico={}
   inpath = "/home/ichiro19/Desktop/INFO4/S8/RI/collection_tokens/"
   for filename in os.listdir(inpath) :
     fich = open(inpath + filename, "r")
     d={}
     for line in fich:
       L= line.split()
       for v in L: 
          if v in d :
            d[v] = d[v] +1 
          else :d[v]=1 
     dico[filename]= d     
   return dico  
   
   
dico = dicos() 
for i in dico:
        print (i, dico[i])
