import datetime

def printTimeStamp(name):
    print("Автор програми: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()),"\n")
printTimeStamp("Valeriy Neroznak")

n=int(input("Введите число:"))
s=int((n*(n+1))/2)
print ("Сума всіх цілих чисел складає:", s)