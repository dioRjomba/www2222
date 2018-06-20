import datetime

def printTimeStamp(name):
    print("Автор програми: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()),"\n")
printTimeStamp("Valeriy Neroznak")

def function(m,n):
    d=int(input("Number:"))
    while int(m)%int(d)and int(n)%int(d):
        d-=1
    print(d)
x=int(input())
y=int(input())
function(x,y)
