input_data = input().split()
numbers = [int(x) for x in input_data]
squares = [x**2 for x in numbers if x > 0 and x % 2 != 0]
print(f"Квадраты: {squares}")


