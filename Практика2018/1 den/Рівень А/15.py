import datetime

def printTimeStamp(name):
    print("Автор програми: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()),"\n")
printTimeStamp("Valeriy Neroznak")

a=list(map(int,input("Введіть числа:").split(" ")))
if a[0]==int(0):
  print("Помилка, перше значення не може бути нулем ")
elif int(0) in a:
    x=sum(a)/(len(a)-1)
    print("Середнє значення: %.2f"%x)
