import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp("Valeriy Neroznak")

list1 = [4, 7, 7, 4, 8, 4, 7, 4, 4, 8, 7, 6, 8, 7, 4, 5, 7, 4, 7]
list2 = [[x,list1.count(x)] for x in set(list1)]
list3 = []
for i in range(len(list2)):
    if list2[i][1] >= 1 and list2[i][1] <= 5:
        list3.append(list2[i][0])
list3 = list(set(list3))
print(list3)
