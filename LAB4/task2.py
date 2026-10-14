cena=int(input())
age=int(input())
if 0>age>120 and cena<=0:
    print('Ошибка')
else:
    if 0<=age<=5:
        cena=0
    elif 6<=age<=17:
        cena=cena/2
    elif 18<=age<=59:
        cena==cena
    elif 60<=age<=120:
        cena=cena/70*100
    print(f"Стоимость: {cena}руб")



