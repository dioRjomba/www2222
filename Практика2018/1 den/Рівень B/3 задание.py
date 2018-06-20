import datetime

def printTimeStamp(name):
    print("Автор програми: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()),"\n")
printTimeStamp("Valeriy Neroznak")

c=0
print("0 градусів Цельсія еквівалентно 32 градусів Фаренгейт")
for i in range(10):
    c += 10
    k = c *float(1.8)+32
    f =k
    print(c, "градусів Цельсія еквівалентно %.f" %f, "градусів Фаренгейт")
