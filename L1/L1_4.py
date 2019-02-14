import os
import math
from functools import reduce 

#print (os.getcwd())

sample1File = open("L1/sample1.txt", "r")
sample1 = sample1File.read().split()

sample2File = open("L1/sample2.txt", "r")
sample2 = sample2File.read().split()

def calcMean(numberList):
    sum = reduce(lambda a,b:float(a)+float(b), numberList)
    return sum/len(numberList)

def calcStdDev(numberList):
    mean = calcMean(numberList)
    sigma = 0
    for num in numberList:
        diffSqr = (float(num) - mean)**2
        sigma += diffSqr
    div = sigma / len(numberList)
    return math.sqrt(div)


print ("Sample1: " +str(calcStdDev(sample1)))
print ("Sample2: " +str(calcStdDev(sample2)))
