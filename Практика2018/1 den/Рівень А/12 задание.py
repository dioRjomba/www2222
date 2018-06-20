import datetime

def printTimeStamp(name):
    print("Автор програми: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()),"\n")
printTimeStamp("Valeriy Neroznak")

z=int(input("Введіть секунди: "))
v=int(input("Введіть хвилини: "))
x=int(input("Введіть години: "))
c=int(input("Введіть дні: "))
s=z+(x*3600)+(c*86400)+(v*60)
print(s,"\nзагальна кількість секунд")
