import datetime

def printTimeStamp(name):
    print("Автор програми: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()),"\n")
printTimeStamp("Valeriy Neroznak")

result = ("")
q = int(input("Введите число: "))
while q != 0:
    res = q%2
    result =result + str(res)
    q = q//2
f=result[::-1]
print(f)
