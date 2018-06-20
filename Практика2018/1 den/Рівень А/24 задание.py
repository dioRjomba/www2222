import datetime

def printTimeStamp(name):
    print("Автор програми: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()), "\n")
printTimeStamp("Valeriy Neroznak")

import math

s = float(input('Довжина сторони: '))
n = float(input('Кількість сторін: '))

print("Площа: %.2f"%((n * s**2) / math.tan(4)* (math.pi /n)),"м**2")

