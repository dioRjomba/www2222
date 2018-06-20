import datetime

def printTimeStamp(name):
    print("Автор програми: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()),"\n")
printTimeStamp("Kharchenko Vasil")


def hos(x, y):
    if x == y:
        return x
    elif x > y:
        return GCD(x - y, y)
    elif x < y:
        return hos(x, y - x)
x=input()
y=input()
print(hos(x, y))

