def s(slow):
    if "ф" in slow:
        return True
    else:
        return False
while True:
    slov=input("Введите слово: ")
    if s(slov):
        print("Ого! Это редкое слово!")
    else:
        print("Эх, это не очень редкое слово...")
