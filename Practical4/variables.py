
#Created on Wed Mar 13 09:29:01 2019

#@author: 11601

a=812
b=812812
c=b/7
d=c/11
e=d/13


X=(a==b)
Y=(a==e)
print(X,Y)
print((X and not Y)or(Y and not X))
print(X!=Y)

