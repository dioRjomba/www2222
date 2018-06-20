import datetime

def printTimeStamp(name):
    print("Автор програми: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()),"\n")
printTimeStamp("Valeriy Neroznak")

import math as m

t1=m.cos(m.radians(float(input("Введіть ширину першої точки: "))))
g1=m.cos(m.radians(float(input("Введіть довготу першої точки: "))))
t2=m.cos(m.radians(float(input("Введіть ширину другої точки: "))))
g2=m.cos(m.radians(float(input("Введіть довготу другої точки: "))))


vb=6371.01*m.acos(m.sin(t1)*m.sin(t2)+m.cos(t1)*m.cos(t2)*m.cos(g1-g2))
print("Відстань між точками %.3f"%vb, "кілометрів")
