zero=0
pol=0
otric=0
kol=int(input())
for n in range(kol):
    n=float(input())
    if n<0:
        otric+=1
    elif n==0:
        zero+=1
    elif n>0:
        pol+=1
print(f'Выше нуля:{pol}\nНиже нуля:{otric}\nРавны нулю:{zero}')
