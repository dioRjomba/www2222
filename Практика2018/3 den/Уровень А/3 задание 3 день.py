import random as r
import itertools as i
import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp("Valeriy Neroznak")

lis = [6, 9, 12, 7, 78, 50]
r.shuffle(lis)
print(lis)
print(list(i.permutations(lis)))
for i in range(8):
    lis.append(r.randint(0, 1000))
print(' ')
print(lis)
