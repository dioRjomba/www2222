import datetime

def printTimeStamp(name):
    print("Автор програми: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()),"\n")
printTimeStamp("Kharchenko Vasil")

t = open("text.txt", 'a')
t.write("Kharchenko Vasil")

t.close()


