import datetime

def printTimeStamp(name):
    print("Автор програми: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()),"\n")
printTimeStamp("Valeriy Neroznak")

"""n=int(input())
def fact(n):
    factors = []
    d = 2
    m=n
    if (m<d):
        print ("Помилка")
        return
    else:
        while( d * d <= n)and(m>=2):
            if n%d ==0:
                factors.append(n)
                n =n// d
            else:
                d+=1
    print("{} = {}".format(m, factors))
fact(n)"""
n=int(input())
f=2
while f<=2:
    if n%f==0:
        f.append(n)
        n = n // d
    else:
        f += 1

print(f)
