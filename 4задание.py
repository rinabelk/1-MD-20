import random

oshibka=0
answer=0
col=0
while oshibka<3:
    number1=random.randint(0, 10)
    number2=random.randint(0, 10)
    operator="+"
    qwest=f"{number1}{operator}{number2} = "
    slov=int(input(qwest))
    answer=number1+number2
    if slov==answer:
        print ("Правильно!")
        col+=1
    else:
        print("Ответ неверный :(")
        oshibka+=1
print("Игра окончена. Правильных ответов: ", col)

