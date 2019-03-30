# -*- coding: utf-8 -*-
#"""
#Created on Wed Mar 13 10:44:30 2019
#
#@author: 11601
#"""
#

n=3500
i=12
answer=str(n)+"="
while i>=0:
 if n>=2**i:
    n=n-2**i
    answer=answer+"+2**"+str(i)
    i=i-1
 else:
    i=i-1
    
print(answer)
    