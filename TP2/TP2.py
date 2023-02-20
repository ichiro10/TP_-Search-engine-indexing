import os 
import json  
import math
from nltk.stem.porter import *
from tqdm import tqdm
import numpy as np


#****** Q1 ********	   

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
   
   
def anti_dic():
    infile = "/home/ichiro19/Desktop/INFO4/S8/RI/cacm/common_words"
    fileHandler = open (infile, "r")
    line = fileHandler.readline()
    d={}
    while line:
      l = line.strip('\r\n')
      L= line.split()
      d[L[0]]=1	   
      line = fileHandler.readline()
    return d   
	   
#****** Q2 ********
	   
def filtering(dic ,anti_dic):
    for i in dic:
       dic_file= dic[i]
       for j in list(dic_file): 
           if j in anti_dic :
              dic[i].pop(j)
           else :   
            stemmer = PorterStemmer()   
            racine = stemmer.stem(j)
            dic[i][racine]=dic[i][j]
            dic[i].pop(j)   
           
    return dic           
    
#****** Q3,Q4,Q4' ********	  
     
def vocabulaire():
    d={}
    anti_dicc = anti_dic()
    dic = dicos()
    N= len(dic.keys())
    dicf=filtering(dic ,anti_dicc)
    for i in dicf: 
       dic_file = {}       
       for j in dicf[i] : 
            dic_file[j] = 1
       for v in dic_file: 
          if v in d :
            d[v] = d[v] +1 
          else : d[v]=1       
    for i in d :
       d[i]= math.log(N/d[i])
      
    with open("vocabulaire.json", 'w') as fp:
      json.dump(d, fp)
    fp.close()
     
#****** Q5 ********	
         
def get_idf(v ,d):
    return d[v]       
             
def vecteur_doc():
    with open('vocabulaire.json', 'r') as fp:
       dc = json.load(fp)
    fp.close()
    anti_dicc = anti_dic()
    dic = dicos()
    dicf=filtering(dic ,anti_dicc)
    d={}
    for doc in tqdm(dicf) :
        d[doc]={}
        for v in dicf[doc]:
             idf=get_idf(v, dc)
             d[doc][v]=  dicf[doc][v]*idf
    return d
    
#****** Q6 ********	      
 
def index_inverse(dic_vocab, dic_vecteur):
    d={}
    for v in dic_vocab:
       d1={}
       for doc in dic_vecteur: 
           if v in dic_vecteur[doc]:
                d1[doc]=dic_vecteur[doc][v]
       d[v]= d1
    with open("index_inverse.json", 'w') as fp:
      json.dump(d, fp)
    fp.close()   
    return d            
    
    
#****** Q7 ********	       
def norme_doc(dic_vecteur):
    d={}
    for doc in dic_vecteur:
        S=0  
        for v in dic_vecteur[doc]:
            S+= dic_vecteur[doc][v]
        norme = math.sqrt(S)                          
        d[doc]=norme
    return d            
         
           
           
         
 
          
