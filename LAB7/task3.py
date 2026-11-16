user_input=input()
number=int(input())
list=list(map(int, user_input.split()))
index=[i for i,x in enumerate(list) if x==number]
print(f'Индексы: {index}')

