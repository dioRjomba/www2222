import datetime as d

def printTimeStamp(name):
    print("Автор програми: " + name)
    print("Час компіляції: " + str(d.datetime.now()),"\n")
printTimeStamp("Valeriy Neroznak")

рік=int(input("Введіть рік: "))
місяць=int(input("Введіть місяць: "))
день=int(input("Введіть день: "))
дата=d.date(рік, місяць, день)
f=дата+d.timedelta(days=1)

print("Завтрішня дата",f)
