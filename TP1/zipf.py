import os
import math
from operator import itemgetter  

def dicos():

   dico={}
   inpath = "/home/ichiro19/Desktop/INFO4/S8/RI/collection_tokens/"
   for filename in os.listdir(inpath) :
     fich = open(inpath + filename, "r")
     for line in fich:
       L= line.split()
       for v in L: 
          if v in dico :
            dico[v] = dico[v] +1 
          else :dico[v]=1 
   return dico  
   
   
   
d=dicos()
dord=reversed(sorted(d.items(), key = itemgetter(1)))
L=[]
for elem in reversed(sorted(d.items(), key = itemgetter(1))):
          L.append(elem)
        
for i in range(10):
   print(L[i])
   
M = 0
for j in range(len(L)):
   M+=L[j][1]           
   
   
print("la taille du vocabulaire My =" , len(L) )    
print("le nombre d'occurence du vocabulaire M =", M)    
print("lambda =", M/math.log(len(L)))  

          
          
  
            

 
 
