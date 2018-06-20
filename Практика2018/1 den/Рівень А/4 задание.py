import datetime

def printTimeStamp(name):
    print("Автор програми: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()),"\n")
printTimeStamp("Valeriy Neroznak")

Голосні = ["a","o","e","i","u"]
Буква = input("Введіть букву: ")
x=len(Буква)
if x == 1:
    if Буква in Голосні:
        print("Введенна буква являється голосною.")
    elif Буква in "y":
        print("Введенна буква, в деяких випадках, являється і голосною, і приголосною.")
    else:
        print("Введенна буква являється приголосною.")
else:
    print("Некоректний введення")
