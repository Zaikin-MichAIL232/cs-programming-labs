
n = int(input())
odd_count = 0
current_row = [1]
for i in range(n):
    print(" ".join(map(str, current_row)))
    for num in current_row:
        if num % 2 != 0:
            odd_count += 1
    if i < n - 1:
        next_row = [1]
        for j in range(len(current_row) - 1):
            next_row.append(current_row[j] + current_row[j + 1])
        next_row.append(1)
        current_row = next_row
print(f"Нечетных элементов: {odd_count}")