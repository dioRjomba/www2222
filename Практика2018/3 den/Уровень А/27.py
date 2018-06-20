import datetime

def printTimeStamp(name):
    print("Автор програми: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()),"\n")
printTimeStamp("Kharchenko Vasil")

import random

t = open("text.txt", 'r')
text = t.readlines()

password = text[random.randint(0, len(text) - 1)].title() + text[random.randint(0, len(text) - 1)]
print(password)
t.close()



