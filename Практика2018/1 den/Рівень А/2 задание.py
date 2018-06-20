import datetime

def printTimeStamp(name):
    print("Автор програми: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()),"\n")
printTimeStamp("Valeriy Neroznak")

Ріст= float(input("Введіть ріст в метрах: "))
Маса= float(input("Введіть масу в кілограмах: "))
Тотал=(Маса)/(Ріст**2)
ІМТ= round(Тотал,7)
print(ІМТ)