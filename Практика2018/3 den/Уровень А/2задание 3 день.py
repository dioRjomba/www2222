import datetime

def printTimeStamp(name):
    print("Автор програми: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()),"\n")
printTimeStamp("Valeriy Neroznak")

import random
lis1=[]
def i():
    for i in range(3):
        q=random.randint(0,9)
        w=random.randint(0,9)
        e=random.randint(0,9)
        r=random.randint(0,9)
        t=random.randint(0,9)
        y=random.randint(0,9)
        u=random.randint(0,9)
        i=random.randint(0,9)
        o=random.randint(0,9)
        lis=(str("+38(0"+str(q)+str(w)+")"+str(e)+str(r)+str(t)+"-"+str(y)+str(u)+"-"+str(i)+str(o)))
    print(lis)
i()


"""import random
lis=[]
def i():
    for i in range(3):
        q=random.randint(0,9)
        w=random.randint(0,9)
        e=random.randint(0,9)
        r=random.randint(0,9)
        t=random.randint(0,9)
        y=random.randint(0,9)
        u=random.randint(0,9)
        i=random.randint(0,9)
        o=random.randint(0,9)
        lis=[str("+38(0"+str(q)+str(w)+")"+str(e)+str(r)+str(t)+"-"+str(y)+str(u)+"-"+str(i)+str(o))]
        print(lis)
i()"""
