rez=" "
while True:
    slov=input("Введите слово. Если слов достаточно до введите stop: ")
    if slov=="stop":
        break
    else:
        rez = rez + " " + slov
print("Объединим слова: ", rez)