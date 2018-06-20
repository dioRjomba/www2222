import datetime

def printTimeStamp(name):
    print("Автор програми: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()),"\n")
printTimeStamp("Valeriy Neroznak")

import functools as f
a = list(map(int, input("Введите 12 чисел: ").split()))
b=[1,3,1,3,1,3,1,3,1,3,1,3]
s= list(map(lambda x, y: x * y, a,b))
print(s)
k=f.reduce((lambda x,y: x+y),s)
print("Сума: ",k)

l=10-(k%10)
print("Последняя цифра: ",l)