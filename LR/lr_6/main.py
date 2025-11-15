# Матрица N * N,
# 1. Определить номера столбцов с однинаковыми элементами
import math

def www(x, start):
    a = []
    tmp = None
    for z, q in enumerate(x[start:]):
        if tmp is None:
            tmp = q
        if tmp == q:
            a.append(z + start)
    if len(a) != 1:
        print(a)



matrix = [[1, 2, 0, 2, 3],
          [2, 2, 2, 2, 3],
          [0, 2, 1, 2, 4],
          [1, 2, 1, 2, 5]]

columns = list(map(list, zip(*matrix)))

cc = []
for i in range(len(columns)):
    cc.append([str(columns[i]).count('0'), sum(columns[i]), math.prod(columns[i])])

for i in range(len(cc)):
    www(cc, i)

# 2. Определить положение элементов значение которых является минимальный строке и максимальным столбце на пересечение которых на пересечение которых они стоят (или наоборот)
matrix = [[1, 2, 1],
          [6, 7, 7],
          [2, 9, 1]]

columns = list(map(list, zip(*matrix)))

for i in range(len(matrix)):
    for y in range(len(columns)):
        if max(matrix[i]) == min(columns[y]):
            print(i + 1, y + 1)



# 3. Матрица квадратная, определить является ли она магическим квадратом
matrix = [[1, 2, 3],
          [3, 1, 2],
          [2, 3, 1]]

columns = list(map(list, zip(*matrix)))

for i in range(len(matrix)):
    if sum(matrix[i]) == sum(columns[i]):
        continue
    else:
        print("Не равно")
        exit(0)

print("Равно")