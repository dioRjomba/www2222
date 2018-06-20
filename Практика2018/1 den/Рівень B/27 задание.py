import datetime

def printTimeStamp(name):
    print("Автор програми: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()),"\n")
printTimeStamp("Valeriy Neroznak")

for i in range(1,11):
    print(" ")
    for z in range(1,11):
        print(i*z, end="\t")
