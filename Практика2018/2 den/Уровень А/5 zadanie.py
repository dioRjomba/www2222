import datetime

def printTimeStamp(name):
    print("Автор програми: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()),"\n")
printTimeStamp("Valeriy Neroznak")


import operator
x = {1: 6, 3: 4, 4: 3, 2: 1, 0: 0, 5: 1, 100: 0, 6: 30}
sorted_x = sorted(x.items(), key=operator.itemgetter(0))
sorted_x_r = sorted(x.items(), key=operator.itemgetter(0),reverse=True)
print("Сортування за значенням :",sorted_x)
print("Сортування за значенням (реверс) :",sorted_x_r)
f=sorted_x+sorted_x_r

print("Конкатенація :",sorted_x+sorted_x_r)
