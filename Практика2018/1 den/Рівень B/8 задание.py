import datetime

def printTimeStamp(name):
    print("Автор програми: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()),"\n")
printTimeStamp("Valeriy Neroznak")

месяц = int(input("Введіть місяць свого дня народження: "))
число = int(input("Введіть свій день народження: "))
if  месяц == 1:
    if 1<= число <= 19:
        print("Capricon")
    elif 20 <= число <=31:
        print("Aquarius")
    else:
        print("Введенне не правильне число")
elif  месяц == 2:
    if 1<= число <= 18:
        print("Aquarius")
    elif 19 <= число <= 29:
        print("Pisces")
    else:
        print("Введенне не правильне число")

elif  месяц == 3:
    if 1<= число <= 20:
        print("Pisces")
    elif 21 <= число <= 31:
        print("Aries")
    else:
        print("Введенне не правильне число")

elif  месяц == 4:
    if 1<= число <= 19:
        print("Aries")
    elif 20 <= число <= 30:
        print("Taurus")
    else:
        print("Введенне не правильне число")

elif  месяц == 5:
    if 1<= число <= 20:
        print("Taurus")
    elif 21 <= число <= 31:
        print("Gemini")
    else:
        print("Введенне не правильне число")

elif  месяц == 6:
    if 1<= число <= 20:
        print("Gemini")
    elif 21 <= число <= 30:
        print("Cancer")
    else:
        print("Введенне не правильне число")

elif  месяц == 7:
    if 1<= число <= 22:
        print("Cancer")
    elif 23 <= число <= 31:
        print("Leo")
    else:
        print("Введенне не правильне число")

elif  месяц == 8:
    if 1<= число <= 22:
        print("Leo")
    elif 23 <= число <= 31:
        print("Virgo")
    else:
        print("Введенне не правильне число")

elif  месяц == 9:
    if 1 <= число <= 22:
        print("Virgo")
    elif 21 <= число <= 30:
        print("Libra")
    else:
        print("Введенне не правильне число")

elif  месяц == 10:
    if 1<= число <= 22:
        print("Libra")
    elif 21 <= число <= 31:
        print("Scorpio")
    else:
        print("Введенне не правильне число")

elif  месяц == 11:
    if 1<= число <= 21:
        print("Scorpio")
    elif 21 <= число <= 30:
        print("Sagittarius")
    else:
        print("Введенне не правильне число")

elif  месяц == 12:
    if 1<= число <= 21:
        print("Sagittarius")
    elif 22 <= число <= 31:
        print("Capricon")
    else:
        print("Введенне не правильне число")
else:
    print("Введений не правельний місяць")
