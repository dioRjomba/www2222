import datetime

def printTimeStamp(name):
    print("Автор програми: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()),"\n")
printTimeStamp("Valeriy Neroznak")

a=input("Месяц:")
if a in ["Квітень","Червень","Вересень","Листопад"]:
    print("В цьому місяці 30 днів")
elif a in ["Січень","Березень","Травень","Липень","Серпень","Жовтень","Грудень"]:
    print("В цьому місяці 31 днів")
else:
    print("В цьому місяці 29 або 30 днів")
