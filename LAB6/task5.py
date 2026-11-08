n = int(input())
if n < 1 or n > 10:
    print("Ошибка")
else:
    i = 0
    while i < n:
        row = str(i)
        j = 1
        while j < n:
            if i > j:
                dist = i - j
            else:
                dist = j - i
            row = row + " " + str(dist)
            j = j + 1
        print(row)
        i = i + 1