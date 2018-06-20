import datetime

def printTimeStamp(name):
    print("Автор програми: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()),"\n")
printTimeStamp("Valeriy Neroznak")

length = 17

def printline(x):
    space = (length - x) / 2
    i = 0
    j = 0
    line = " "
    while i < space:
        line = line + " "
        i += 1
    while j < x:
        line = line + "X"
        j += 1
    print(line)

s = 3
l = 3
while s > -6:
    printline(l)
    l = l + 2 * s
    s = s - 1
    if (l == 15):
        s = s + 1
