import datetime

def printTimeStamp(name):
    print("Автор програми: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()),"\n")
printTimeStamp("Valeriy Neroznak")

a = int(input('Введіть кількість секунд:'))
d = a//86400
h = (a//3600)%24
m = (a//60)%60
s = a%60

if d<10:
    d = str('0' + str(d))
else:
    d = str(d)
if h<12:
    h = str('0' + str(h))
else:
    h = str(h)
if m<10:
    m = str('0' + str(m))
else:
    m = str(m)
if s<10:
    s = str('0' + str(s))
else:
    s = str(s)
print(d,':',h,':',m,':',s)
