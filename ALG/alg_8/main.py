# Global. Работа с функциями
# 1. Дан список целых элементов, сформировать новый список из элементов которых нечётных кол-во делителей
"""
a = [34, 1, 34, 4]
b = []

def tmp(x):
    c = 0
    for i in range(1, x + 1):
        if x % i == 0:
            c += 1
    return c

for i in a:
    if tmp(i) % 2 != 0:
        b.append(i)

print(b)
"""
# 2. В списке целые числа определить кол-во чисел у которых суммы цифр простое число
"""
def suim(x):
    return sum(map(int, str(x)))

def tmp(x):
    c = 0
    for i in range(2, x):
        if x % i == 0:
            c += 1
    return bool(c)

a = [123, 122, 34, 77] #2
counter = 0
for i in a:
    if tmp(suim(i)):
       counter += 1
print(counter)
"""
# 3. На вход подаётся строка из слов разделённым пробелом, выдать слова у которых первая и последняя буква равны п длинна чётная
# регистр не
"""
s = "слово fuf дддД"

def tmp(q):
    return q[0] == q[len(q) - 1] and len(q) % 2 == 0

for i in s.split(" "):
    if tmp(i.lower()):
        print(i)
"""
# 4. Рекурсия. Вычислить функцию n элементов арифметической прогрессии (min shag max)
"""
def tmp(mi, shag, ma, c, count = 0):
    c.append(mi)
    if count == ma:
        print(sum(c))
    else:
        tmp(mi + shag, shag, ma, c, count+1)

tmp(5, 6, 3, [])
"""

