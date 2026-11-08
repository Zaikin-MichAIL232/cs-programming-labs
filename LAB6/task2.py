n = int(input())
if n < 2:
    print("Не простое")
else:
    prime = True
    d = 2
    while d * d <= n:
        if n % d == 0:
            prime = False
            break
        d += 1
    if prime:
        print("Простое")
    else:
        print("Не простое")