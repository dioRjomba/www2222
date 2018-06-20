import datetime

def printTimeStamp(name):
    print("Автор програми: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()),"\n")
printTimeStamp("Valeriy Neroznak")

рік = int(input("Введіть рік: "))
x=(рік%100==0)
y=(рік%400!=0)
z=(рік %4!=0)
if x or (y and z):
    print(рік,"Звичайний рік")
else:
    print(рік,"Високосний рік")