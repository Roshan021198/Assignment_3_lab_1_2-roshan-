# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 00:19:44 2020

@author: ROSHAN
"""

""" no of words in a string
    no of character in a string
    percentage of string """
    
s=input("enter a string ")
char = 0
word = 1
for i in s:
    char=char+1
    if i == ' ':
        word=word+1
        
print("number of words = ",word)
print("number of characters = ",char)