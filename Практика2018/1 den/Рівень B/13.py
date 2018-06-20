import datetime

def printTimeStamp(name):
    print("Автор програми: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()),"\n")
printTimeStamp("Valeriy Neroznak")

import math as m
a=1015
b=719.1
c=797.1
p=(a+b+c)/2
s=m.sqrt(p*(p-a)*(p-b)*(p-c))

print("Площа трикутника : %.2f"%s,"км**2")