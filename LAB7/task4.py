rows, cols = map(int, input().split())
matrix = []
for _ in range(rows):
    row_data = list(map(int, input().split()))
    matrix.append(row_data)
row_sums = []
for r in range(rows):
    current_sum = 0
    for c in range(cols):
        current_sum += matrix[r][c]
    row_sums.append(current_sum)
col_sums = []
for c in range(cols):
    current_sum = 0
    for r in range(rows):
        current_sum += matrix[r][c]
    col_sums.append(current_sum)
print(f"Суммы строк: {row_sums}")
print(f"Суммы столбцов: {col_sums}")