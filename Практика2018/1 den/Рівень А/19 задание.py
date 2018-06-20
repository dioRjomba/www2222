import datetime

def printTimeStamp(name):
    print("Автор програми: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()),"\n")
printTimeStamp("Valeriy Neroznak")

import time as t

time = t.localtime()
asc = t.asctime(time)
print ("Поточний час:" , asc)