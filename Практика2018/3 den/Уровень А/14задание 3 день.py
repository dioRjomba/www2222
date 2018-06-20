import datetime

def printTimeStamp(name):
    print("Автор програми: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()),"\n")
printTimeStamp("Valeriy Neroznak")

def Fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a=(Fib(n-1)+Fib(n-2))
        return(a)

x=int(input("Введіть число: "))
k=Fib(x)
print(k)
