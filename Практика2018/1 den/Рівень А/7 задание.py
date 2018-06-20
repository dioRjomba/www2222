import datetime

def printTimeStamp(name):
    print("Автор програми: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()),"\n")
printTimeStamp("Valeriy Neroznak")

Цельсія= float(input("Введіть температуру в градусах цельсія: "))
Кельвіна=(Цельсія+(273.15))
Фаренгейта=(Цельсія*1.8+32)
print("Еквівалентна температура по Кельвіну :",Кельвіна,"K")
print("Еквівалентна температура по Фаренгейту :",Фаренгейта,"°F")