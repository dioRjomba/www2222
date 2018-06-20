import datetime

def printTimeStamp(name):
    print("Автор програми: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()),"\n")
printTimeStamp("Valeriy Neroznak")

import math
a = float(input("Введіть перше число:"))
b = float(input("Введіть друге число:"))
s=(a+b)
r=(b-a)
m=(a*b)
d=(a//b)
k=(a%b)
l=math.log10(a)
t=(a**b)
print("\nСума: ",s, "\nРізниця: ",r,"\nЧастка: ",d,"\nОстача: ",k, "\nДобуток: ",m,"\nЛогарифм :",l,"\nСтепінь: ",t)