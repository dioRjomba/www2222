import datetime

def printTimeStamp(name):
    print("Автор програми: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()),"\n")
printTimeStamp("Valeriy Neroznak")

a=float(input("Гроші:"))
b=a%float(0.5)
b1=b%float(0.25)
a1 = a // float(0.50)
a2 = b // float(0.25)
a3 = b1 // float(0.10)

if b >0:
    if b % float(0.25)==0:
        print("Give 0.50 ",str(a1)+" times and 0.25 "+str(a2)+" times")
    elif b % float(0.25)!= float(0.0) and  b1 % float(0.10)==float(0.0) :
        print("Give 0.50 " + str(a1) + " times and 0.25 " + str(a2) + " times and 0.10 "+str(a3)+" times")
    elif b1 % float(0.10)!=float(0.0) :
        print("Give 0.50 " + str(a1) + " times and 0.25 " + str(a2) + " times and 0.10 " + str(a3) + " times"+str())
elif b == float(0.0):
    print("Give 0.50 "+str(int(a1))+" times")