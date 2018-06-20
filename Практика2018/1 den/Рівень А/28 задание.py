import datetime

def printTimeStamp(name):
    print("Автор програми: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()),"\n")
printTimeStamp("Valeriy Neroznak")

h=str(input('Зараз вихідний? Напишіть "Так" або "Ні"\n'))
f=str(input('Ви у  відпустці? Напишіть "Так" або "Ні"\n'))

if h== 'Так' or f== 'Так':
  print ('Не вмикати будильник')
else:
  print ('Увімкнути будильник')
