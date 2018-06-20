import datetime


def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp("Valeriy Neroznak")


вода = int(input("вода:"))
гроші = 20
if вода<=30:
    гроші+=float(вода*9.86)
elif 30<вода<=50:
    гроші+=float((вода-30)*11.22+295.8)
elif 50<вода<=60:
    гроші += float((вода - 50) * 13.06+520.2)
elif вода>60:
    гроші+=float((вода-60)*17.89+652.8)

print("Потрібно заплатити:", гроші)


