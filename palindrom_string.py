# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 23:51:14 2020

@author: ROSHAN
"""

s=input("enter a string ")
s1=list(s)
rev= s1[::-1]
rev1="".join(rev) 

if(s==rev1):
    print("palindrom string")
else:
    print("not a palindrom string")
