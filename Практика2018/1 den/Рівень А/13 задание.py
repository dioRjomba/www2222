import datetime

def printTimeStamp(name):
    print("Автор програми: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()),"\n")
printTimeStamp("Valeriy Neroznak")

x=list(map(int,input().split()))
x=sorted(x)
min=min(x)
max=max(x)
summ=sum(x)
summ1=summ-max
summ2=summ-min
print("Сортування від меншого до більшого: ",x)
print("Мінімальне значення: ",min)
print("Максимальне значення: ",max)
print("Сума всіх значень: ",summ)
print("Сума всіх значень без максимального значення: ",summ1)
print("Сума всіх значень без мінімального значення: ",summ2)
