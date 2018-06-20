import datetime

def printTimeStamp(name):
    print("Автор програми: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()),"\n")
printTimeStamp("Valeriy Neroznak")

куп_штучку=int(input("Кількість штучок: "))
куп_штукенцію=int(input("Кількість штукенцій: "))

штучка= 75
штукенція = 112

вага_штучки= (куп_штучку*штучка)
ваша_штукенції= (куп_штукенцію*штукенція)
вага=вага_штучки+ваша_штукенції
print(вага,"грам")

