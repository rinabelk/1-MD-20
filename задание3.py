def s(slow):
    if "ф" in slow:
        return True
    else:
        return False
while True:
    slov=input("Введите слово. Для выхода из цикла напишите 'stop': ")
    if slov=='stop':
        break
    if s(slov):
        print("Ого! Это редкое слово!")
    else:
        print("Эх, это не очень редкое слово...")
