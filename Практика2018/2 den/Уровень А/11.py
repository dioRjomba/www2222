import datetime

def printTimeStamp(name):
    print("Автор програми: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()),"\n")
printTimeStamp("Valeriy Neroznak")

import winsound
import itertools as i

x=[(659), (659), (659), (523), (659), (784),
(392), (523), (392), (330), (440), (494),
(466), (440), (392), (659), (784), (880),
(698), (784), (659), (523), (587), (494),1000]
y=[(250), (250), (300), (250), (250), (300),
(300), (275), (275), (275), (250), (250),
(275), (275), (275), (250), (250), (275),
(275), (225), (250), (250), (225), (225),1000]
n=0
for item in i.count(1):
    n=n+1
    if n>23:
        break
    else:
        g=x[0]+x[n]
        f=y[0]+y[n]

    winsound.Beep(g,f)
