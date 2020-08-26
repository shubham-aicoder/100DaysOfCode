import math
import os
import random
import re
import sys
# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    d1={}
    d2={}
    c=0
    for word in magazine:
        if word not in d1:
            d1[word]=0
        d1[word]+=1
    for word in note:
        if word not in d2:
            d2[word]=0
        d2[word]+=1
    
    try:
        for i in range(len(note)):
            if d2[note[i]]==d1[note[i]]:
                c+=1
        if c==len(note):
            print("Yes")
        else:
            print("No")
    except:
        print("No")
            
    
    
            

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
