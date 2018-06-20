import datetime

def printTimeStamp(name):
    print("Автор програми: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()),"\n")
printTimeStamp("Valeriy Neroznak")

a = int(input("Перша сторона = "))
b = int(input("Друга сторона = "))
c = int(input("Третя сторона = "))

if a + b <= c or a + c <= b or b + c <= a:
    print("Трикутник не існує")
elif a != b and a != c and b != c:
    print("Різносторонній")
elif a == b == c:
    print("Рівносторонній")
else:
    print("Рівнобедренний")