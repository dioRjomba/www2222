import datetime

def printTimeStamp(name):
    print("Автор програми: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()),"\n")
printTimeStamp("Valeriy Neroznak")

import math

M=57
T0=4
p=1.038
c=3.7
K=5400
ty=100
tw=70
t=(((M**float(2/3))*c*(p**float(1/3)))/ 5400*(math.pi**2)*(4*math.pi/3)**(2/3))*math.log10(0.76*((T0-ty)/(tw-ty)))
t=t*60
print("%.2f"%t,"хвилин")