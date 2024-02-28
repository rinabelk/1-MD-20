n=int(input ("Ведите количество слов: "))
rez=""
for i in range(n):
    slov=input(f"Введите слово:")
    rez=rez+" "+slov
print ("Обединим слова:", rez)