mat = [
    [5, 3, 1],
    [2, 4, 6],
    [9, 7, 5]
]
from math import prod
# 1. Найти сумму в каждой строке

rs = []
for r in mat:
    rs.append(sum(r))

print(rs)

# 2. Количество столбцов, в которых сумма больше чем произведения

pc = 0
for c in zip(*mat):
    if sum(c) > prod(c):
        print("Cумма больше произведения")
    elif sum(c) < prod(c):
        print("Cумма меньше произведения")
    else:
        print("Равное кол-во")

print(pc)

# 3. Номера строк, в которых элементы упорядочены по убыванию

dr = []
for i, r in enumerate(mat):
    flag = True
    for j in range(len(r) - 1):
        if not (r[j] > r[j+1]):
            flag = False
            break

    if flag:
        dr.append(i)

print(dr)
