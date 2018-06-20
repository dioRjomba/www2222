import datetime

def printTimeStamp(name):
    print("Автор програми: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()),"\n")
printTimeStamp("Valeriy Neroznak")

t=float(input("Введіть температуру в градусах Цельсія(не менше чим 10ºС): "))
v=float(input("Введіть швидкість вітру в км/год(не менше чим 4.8): "))
if t<=10 and v>4.8:
    WCI = (13.12 + 0.6215*t-11.37*(v**0.16)+0.3965*t*(v**0.16))
    print("Індекс прохолодності вітру: %.f"%WCI)
else:
    print("\nВведені не вірні дані, будь ласка прочитайте умову ")