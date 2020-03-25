# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 00:11:13 2020

@author: ROSHAN
"""

def cap(s):
    res=''
    i=True
    for char in s:
        if i:
            res = res + char.upper()
        else:
            res = res + char.lower()
        if i != ' ':
            i = not i
    return res

s=input("enter a string ")
print(cap(s))