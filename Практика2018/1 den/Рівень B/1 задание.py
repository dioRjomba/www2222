import datetime

def printTimeStamp(name):
    print("Автор програми: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()),"\n")
printTimeStamp("Valeriy Neroznak")

p= float(input("Давление: "))
v= float(input("Обьем: "))
r = 8.314
k = float(input("Температура в Цельсиях: "))
k = k+273.15
n= float((p*v)/(r*k))
print(n)