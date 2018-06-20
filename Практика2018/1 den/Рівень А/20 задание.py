import datetime

def printTimeStamp(name):
    print("Автор програми: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()),"\n")
printTimeStamp("Valeriy Neroznak")

bread=input("Скільки буханок купляєте?: ")
summa=8.5 * float(bread)
i = (summa * 0.6)
suk= summa - i
print("Хліб коштує: ", summa)
print("Отримана знижка: %.2f"% i)
print("Загальна сума складає: %.2f"% suk)

