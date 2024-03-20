def a(number):
    if number % 5 == 0:
        return True
    else:
        return False


number = int(input("Введите число: "))
if a(number):
    print("Число делится на 5")
else:
    print("Число не делится на 5")

def a(number1):
    try:
        rez = 300 / number1
        return rez
    except ValueError:
        return "Вы ввели не число"
    except ZeroDivisionError:
        return "Вы ввели число 0"
number1=int(input("Введите число: "))
if a(number1):
    print("Введенное число, делится на 300 и равно: ", a(number1))

def n():
    date=input("Введите дату:")
    day, month, year = map(int, date.split("."))
    if day*month == int(str(year)[-2:]):
        return True
    else:
        return False
print(n())

