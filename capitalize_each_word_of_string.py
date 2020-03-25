# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 00:06:04 2020

@author: ROSHAN
"""

import string

s=input("enter a string ")
print(string.capwords(s))
#======================================
#this is another way
s = input("enter string = ")

words = s.split(" ")

s1=[]

for word in words:    
    s1.append(word)

print(string.capwords(" ".join(s1)))

#===================================
#this is another way

s1 = input("enter string = .")
list = [' '.join(word[0].upper() + word[1:] for word in s.split())]
print(" ".join(list))