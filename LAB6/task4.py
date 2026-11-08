n = int(input())
if n < 0:
    print("Ошибка")
else:
    count = 0
    total = 0
    if n == 0:
        count = 1
    while n > 0:
        total = total + n % 10
        n = n // 10
        count = count + 1
    print("Цифр:", count)
    print("Сумма цифр:", total)