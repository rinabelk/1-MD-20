def tesk1():
    countres={
        "Россия": "Москва",
        "Франция": "Париж",
        "Южная Корея": "Сеул",
        "Италия": "Рим"
    }

    for country, capital in countres.items():
        print(f"Все страны и их столицы: {country} - {capital} ")

    country1= input("Введите страну: ")
    for country, capital in countres.items():
        if country1==country:
            print(f'{country1} - столица {capital}')
    print(sorted(countres))
print(tesk1())
def tesk2():
    def score(slovo):

        sum=0
        for letter in slovo.upper():
            if letter in slova:
                sum += int(slova[letter])
        return sum
    slova= {'А': '1', 'В': '1', 'Е': '1', 'И': '1', 'Н': '1', 'О': '1', 'Р': '1', 'С': '1', 'Т': '1', 'Д': '2', 'К': '2', 'Л': '2', 'М': '2', 'П': '2', 'У': '2', 'Б': '3', 'Г': '3', 'Ё': '3', 'Ь': '3', 'Я': '3', 'Й': '4', 'Ы': '4', 'Ж': '5', 'З': '5', 'Х': '5', 'Ц': '5', 'Ч': '5','Ш': '8', 'Э': '8', 'Ю': '8', 'Ф': '10', 'Щ': '10', 'Ъ': '10'}
    slovo=input("Введите слово: ")
    c=score(slovo)
    print(f'Стоимость слова "{slovo}" = {c}')
print(tesk2())



