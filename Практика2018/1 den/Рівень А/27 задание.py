import datetime

def printTimeStamp(name):
    print("Автор програми: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()),"\n")
printTimeStamp("Valeriy Neroznak")

s=input('Папуга говорить? Напишіть Так або Ні\n')
if s == 'Ні':
  print ('Погладьте папугу')
else:
  t=int(input('Котра зараз година? Напишіть число від 0 до 23\n'))
  if s == 'Так'  and 22<=t>=24 or t<=8:
    print ('Накрийте папугу рядниною')
  else:
    print ('Не звертайте уваги на папугу')
