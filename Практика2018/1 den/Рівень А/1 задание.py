import datetime

def printTimeStamp(name):
    print("Автор програми: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()),"\n")
printTimeStamp("Valeriy Neroznak")

litr=float(input("Введіть кількість контейнерів об'єм яких, менше 1 літра: "))
litr2=float(input("Введіть кількість контейнерів об'єм яких, більше 1 літра: "))

summ= litr*0.1
summ2= litr2* 0.25
summm=summ+summ2
print("Отримаєте за повернення контейнерів","%.2f" % summm,"$")
