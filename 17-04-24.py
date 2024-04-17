def task1():
    from PIL import image
    img=image.open("malina.jpg")
    img.show()
    print(img.size)
    print(img.format)
    print(img.mode)
#task1()

def task2():
    from PIL import image
    img=image.open("malina.jpg")
    img1=image.reduce(3)
    img2=image.transformate(image.FLIP_LEFT_RIGHT)
    img3=image.transformate(image.FLIP_TOP_BOTTOM)
    img1.save("malina1.jpg")
    img2.save("malina2.jpg")
    img3.save("malina3.jpg")


