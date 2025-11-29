
from collections import Counter

l = [1, -2, 3, 10, -5, 6, 6]
m = 3

# 1. Наибольшую сумму цепочки из m элементов
"""
ms = []
for i in range(len(l) - m + 1):
    ms.append(sum(l[i:i+m]))

print(max(ms))
"""
# 2. Частота появления каждого элемента
print()
for e, i in Counter(l).items():
    print(f"Число: {e} | Кол-во чисел: {i}")

# 3. Определить элементы встречающиеся 1 раз
"""
uniq = []
for k, v in Counter(l).items():
    if v == 1:
        uniq.append(k)

print(uniq)
"""
# 4. Определить наибольшую сумму из элементов
"""
curr = glob = l[0]
for x in l[1:]:
    curr = max(x, curr + x)
    glob = max(glob, curr)

print(glob)
"""