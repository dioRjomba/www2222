import datetime

def printTimeStamp(name):
    print("Автор програми: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()),"\n")
printTimeStamp("Valeriy Neroznak")

Рік = int(input("Введіть свій рік народження :"))
Зодиак = (Рік % 12)
if  Зодиак == 0:
    print("Monkey")
elif Зодиак == 1:
    print("Rooster")
elif Зодиак == 2:
    print("Dog")
elif Зодиак == 3:
    print("Pig")
elif Зодиак == 4:
    print("Rat")
elif Зодиак == 5:
    print("Ox")
elif Зодиак == 6:
    print("Tiger")
elif Зодиак == 7:
    print("Rabbit")
elif Зодиак == 8:
    print("Dragon")
elif Зодиак == 9:
    print("Snake")
elif Зодиак == 10:
    print("Horse")
elif Зодиак == 11:
    print("Sheep")
else:
    print("ЦЕ НЕ МОЖЛИВО")