import datetime

def printTimeStamp(name):
    print("Автор програми: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()),"\n")
printTimeStamp("Valeriy Neroznak")

def factorial(n):
    if n==0:
        return 1
    else :
        a=factorial(n-1)*n
        return a


x=int(input("Введіть число:"))
print(factorial(x))
