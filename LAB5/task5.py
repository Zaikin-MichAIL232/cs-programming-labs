total_cost=0
count=0
while True:
    user_input=input()
    if user_input == 'stop':
        break
    cost=int(user_input)
    count+=1
    total_cost+=cost
if count==0:
        print('Покупок нет')
else:
    sr_cost=total_cost/count
    print(f'Общая стоимость:{total_cost}рубС\nКол-во покупок:{count}')
    print(f'Cредняя стоимость:{sr_cost}руб')
