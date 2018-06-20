import datetime

def printTimeStamp(name):
    print("Автор програми: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()),"\n")
printTimeStamp("Valeriy Neroznak")

x=int(input())
if x < 3*10**9:
  print("radio waves")
elif 3*10**9 <= x < 3*10**12:
  print("microwaves")
elif 3*10**12 <= x < 4.3*10**14:
  print("infrared light")
elif 4.3*10**14 <= x < 7.5*10**14:
  print("visible light")
elif 7.5*10**14 <= x < 3*10**17:
  print("ultraviolet light")
elif 3*10**17 <= x < 3*10**19:
  print("X-rays")
elif x >= 3*10**19:
  print("gamma rays")
else: 
  print("error 404")
