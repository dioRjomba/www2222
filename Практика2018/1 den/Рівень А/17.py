import datetime

def printTimeStamp(name):
    print("Автор програми: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()),"\n")
printTimeStamp("Valeriy Neroznak")

рахунок=int(input("Рахунок:"))
один=рахунок*(float(1.14))
два=один*(float(1.14))
три=два*(float(1.14))
print("Річна ставка за 1 год %.2f"%один)
print("Річна ставка за 2 года %.2f"%два)
print("Річна ставка за 3 года %.2f"%три)
