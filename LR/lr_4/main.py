mat = [
    [5, 3, 1],
    [2, 4, 6],
    [9, 7, 5]
]

# 1. Найти сумму в каждой строке
rs = []
for r in mat:
    rs.append(sum(r))

print(rs)

# 2. Количество столбцов, в которых сумма больше 0
pc = 0
for c in zip(*mat):
    if sum(c) > 0:
        pc += 1

print(pc)

# 3. Номера строк, в которых элементы упорядочены по убыванию
dr = []
for i, r in enumerate(mat):
    is_decreasing = True
    for j in range(len(r) - 1):
        if not (r[j] > r[j+1]):
            is_decreasing = False
            break

    if is_decreasing:
        dr.append(i)

print(dr)