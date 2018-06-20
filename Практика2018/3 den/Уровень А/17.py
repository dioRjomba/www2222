import datetime

def printTimeStamp(name):
    print("Автор програми: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()),"\n")
printTimeStamp("Kharchenko Vasil")



def hos(x, y):
    if y == 0:
        return 1
    elif y < 0:
        return 1 / hos(x, y * -1)
    else:
        if y % 2 == 0:
            return hos(x, y / 2) ** 2
        else:
            return x * hos(x, y - 1)

x=int(input())
y=int(input())
print(hos(x, y))

