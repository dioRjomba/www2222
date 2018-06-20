import datetime

def printTimeStamp(name):
    print("Автор програми: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()),"\n")
printTimeStamp("Valeriy Neroznak")

m=float(input("Введіть масу води, яку хочите нагріти: "))
t0=float(input("Введіть початкову температуру води: "))
t1=float(input("Введіть бажану температуру води: "))
t=t1-t0
q=m*t*4.186
print("Потрачена енергія: %.2f"%q,"Дж")
l=q/10**3
vat=l*0.0002777777777778
cost=vat*1.33
print("Вартість нагрітої води: %.4f"%cost,"грн")
