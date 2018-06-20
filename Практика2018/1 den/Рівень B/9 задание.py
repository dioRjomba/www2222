import datetime

def printTimeStamp(name):
    print("Автор програми: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()),"\n")
printTimeStamp("Valeriy Neroznak")


a=input("Введіть номерний знак:")

if a[0:3].isdigit() and isinstance(a[4:6],str)and a[4:6].isupper():
    print("Старіші номерні знаки")
elif isinstance(a[0:2],str) and a[3:5].isdigit()  and a[0:3].isupper():
    print("Нові номерні знаки")
else:
    print("Помилка, введені неправильні дані")
