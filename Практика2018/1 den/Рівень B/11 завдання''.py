import datetime

def printTimeStamp(name):
    print("Автор програми: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()),"\n")
printTimeStamp("Valeriy Neroznak")


гроші = 0
x = 0
while True:
    a = input("Years old:")
    if str(a) == str("-"):
        if x >= 10:
            гроші = гроші - гроші * 0.1
            print("Оплата: %.2f" % гроші)
            break
        else:
            print("Оплата: %.2f" % гроші)
            break
    elif int(a) <= int(3):
        x += 1
    elif int(3) < int(a) < int(12):
        x += 1
        гроші += float(16.00)
    elif int(12) < int(a) < int(60):
        x += 1
        гроші += float(25.00)
    elif int(a) >= int(60):
        x += 1
        гроші += float(18.00)
