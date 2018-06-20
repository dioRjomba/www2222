import datetime

def printTimeStamp(name):
    print("Автор програми: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()),"\n")
printTimeStamp("Kharchenko Vasil")


def hos(x):
    if x == 1:
        return 1
    else:
        return (1 / x) + hos(x - 1)
x=int(input())
print(hos(x))


