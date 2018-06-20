import datetime

def printTimeStamp(name):
    print("Автор програми: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()),"\n")
printTimeStamp("Kharchenko Vasil")




t = open('text.txt', 'r')
for i in range(10):
    print(t.readline())

t.close()


