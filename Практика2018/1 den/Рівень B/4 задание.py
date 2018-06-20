import datetime

def printTimeStamp(name):
    print("Автор програми: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()),"\n")
printTimeStamp("Valeriy Neroznak")

x=int(input("Введіть кількість витрачених хвилин :"))
y=int(input("Введіть кількість витрачених СМС :"))

if x>=200 or y>=50:
    звонки=(x-200)*0.17
    смс=(y-50)*0.15+15
    сумма=звонки+смс
    пдф = сумма+15 * 0.05 + 0.44
    print("Базова плата за користування: %.2f"%сумма,"$")
    print("Загальна плата за користування: %.2f"%пдф,"$")
else:
    print("Тариф складає 15.00$")