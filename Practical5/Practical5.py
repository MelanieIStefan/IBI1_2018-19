## -*- coding: utf-8 -*-
#"""
#Spyder Editor
#
#This is a temporary script file.
#""


#counting AGTC
sequence = 'ATGCTTCAGAAAGGTCTTACG'
sequence = list(sequence)

myDict = {}
for word in sequence:
 if word in myDict:
  myDict[word] += 1
 else:
  myDict[word] = 1

myDict

text = input(myDict)

#plotting
import matplotlib.pyplot as plt
labels = 'A','T','G','C'
a = int(myDict['A'])
g = int(myDict['G'])
t = int(myDict['T'])
c = int(myDict['C'])
sizes = [a, g, t, c]
explode = (0.01, 0.01, 0.01, 0.01)
plt.pie(sizes,explode=explode, labels=labels, autopct='%1.1f%%',shadow=False, startangle=90)
plt.axis('equal')
plt.show()


#reverse split and sort a string 
lyrics = "This is Major Tom to Ground Control Im stepping through the door And I'm floating in a most peculiar way And the stars look very different today"

M = lyrics[:]

M = M[-1::-1]

splitM = M.split(' ')

splitM.sort()

print(splitM)
