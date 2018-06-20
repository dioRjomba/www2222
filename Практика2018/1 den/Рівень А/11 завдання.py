import datetime

def printTimeStamp(name):
    print("Автор програми: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()),"\n")
printTimeStamp("Valeriy Neroznak")

Зріст=float(input("Введість свій зріст в сантиметрах: "))
ЗрістДюйм=Зріст*0.39370078740157
ЗрістФут=ЗрістДюйм*0.08333333333333376

print("Ваш зріст в сантиметрах: ",Зріст, "см")
print("Ваш зріст в дюймах: ","%.2f" % ЗрістДюйм, "дюйм")
print("Ваш зріст в футах: ","%.2f" % ЗрістФут, "фут")