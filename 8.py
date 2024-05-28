def tesk1():
    from PIL import Image

    image = Image.open("открытка.jpg")
    crop1 = image.crop((0, 0, 0, 200))
    crop1.save("редактированное.jpg")
tesk1()

def tesk2():

    import os

    holidays = {
        "Новый год":"newyear.jpg",
        "День Рождения":"birthday.jpg",
        "8 марта":"8march.jpg"
    }

    holiday = input("Какая нужна открытка?")
    if holiday in holidays:
        image1=Image.open(holidays[holiday])
        image1.show
    else:
        print("Такой открытки нет :(")
tesk2()

def tesk3 ():

    -
