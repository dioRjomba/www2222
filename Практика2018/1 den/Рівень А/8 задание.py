import datetime

def printTimeStamp(name):
    print("Автор програми: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()),"\n")
printTimeStamp("Valeriy Neroznak")

Число = input("Введіть 4-х значне число: ")
if len(Число) == 4:
    Сума_числа = sum(int(i) for i in Число)
    print(Сума_числа)
else:
    print("Ви ввели не 4-х значне число")
