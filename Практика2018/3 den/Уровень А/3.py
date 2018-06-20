import datetime
import random
def printTimeStamp(name):
    print("Автор програми: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()),"\n")
printTimeStamp("Kharchenko Vasil")


def пароль():
    пас = ('')
    for i in range(random.randint(8,17)):
        пас += chr(random.randint(33, 127))
    print(пас.encode("ascii"))

for i in range(10):
    пароль()



