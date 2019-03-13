#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 13:00:26 2019

@author: cuijiajun
"""

    
n = int(input ())
i = 16

if n % 2 ==0:
    result = '0+'
    
elif n % 2 > 0 :
    n = n -1 
    result = '1+'
while n > 0:
    while n < 2**i:
          i = i-1
            
    while  i >= 0 and n >= 2**i:
           result = result + '2**'+str (i) + '+'
           n = n - 2**i
           i = i - 1
                


print (result)