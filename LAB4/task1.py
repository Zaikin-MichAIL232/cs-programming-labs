

t1=float(input())
t2=float(input())
if t1>t2:
    print('Охлаждение')
    if t1 < t2:
        print('Нагревание')
        if t1 == t2:
            print('выключен')