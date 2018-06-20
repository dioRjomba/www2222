import datetime

def printTimeStamp(name):
    print("Автор програми: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()),"\n")
printTimeStamp("Kharchenko Vasil")

def hos(x, y):
    if y == 0:
        return x
    else:
        return hos(y, x % y)

x=int(input())
y=int(input())
print(hos(x,y))


