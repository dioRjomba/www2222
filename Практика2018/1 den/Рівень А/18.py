import datetime

def printTimeStamp(name):
    print("Автор програми: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()),"\n")
printTimeStamp("Valeriy Neroznak")

import math as m

h=int(input("Висота:"))
v=m.sqrt((0+float(9.8)*h))
print("%.2f" %v, "м/с")