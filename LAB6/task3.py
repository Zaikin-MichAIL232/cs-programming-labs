n = int(input())
if n < 2:
    print("Ошибка")
else:
    result = ""
    d = 2
    while n > 1:
        if n % d == 0:
            if result != "":
                result = result + " "
            result = result + str(d)
            n = n // d
        else:
            d = d + 1
    print(result)