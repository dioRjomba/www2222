import datetime

def printTimeStamp(name):
    print("Автор програми: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()),"\n")
printTimeStamp("Kharchenko Vasil")




def hos(x, y):
    if y == 0:
        return 1
    else:
        return x * hos(x, y - 1)

x=int(input())
print(hos(x, 10))


