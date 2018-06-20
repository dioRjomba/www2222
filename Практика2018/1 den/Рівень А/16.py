
def printTimeStamp(name):
    print("Автор програми: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()),"\n")
printTimeStamp("Valeriy Neroznak")

д=float(input("Довжина:"))
ш=float(input("Ширина:"))
п=(float(д)*float(ш))
аар=float(п)/100
гектар=float(п)/10000
print("Площа :",п,"м**2")
print("Площа :",гектар,"гектар")
print("Площа :",аар,"аар")
