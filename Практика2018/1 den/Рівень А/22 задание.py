import datetime

def printTimeStamp(name):
    print("Автор програми: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()),"\n")
printTimeStamp("Valeriy Neroznak")

import math
r = float(input("Радіус = "))
print("Площа: %.2f" % (math.pi*r**2))
print("Обєм: %.2f" % (3/4*math.pi*r**3))
