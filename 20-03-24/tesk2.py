def a(number1):
    try:
        rez=300/number1
        return rez
    except ValueError:
        return "Вы ввели не число"
    except ZeroDivisionError:
        return "Вы ввели число 0"



