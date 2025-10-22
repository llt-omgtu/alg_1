# Имеется список их n элементов

# 1. Определить произведение элементов, которые стоят, на нечётных местах, с точки зрения пользователя
"""
a = [1, 2, 3]
tmp = []
for i, c in enumerate(a):
    if (i + 1) % 2 != 0:
        tmp.append(c)
q = 0
for i in tmp:
    q *= i

print(q / len(tmp))
"""
# 2. Найти минимальных размер подпоследовательности состоящих из двоек
"""
a = [3,3,2]
a = [2, 2, 2, 4, 2, 2, 45, 2, 2, 2, 45]
c = 0
n = []
z = []
for i in a:
    if i == 2:
        c += 1
    else:
        n.append(c)
        c = 0
if c != 0:
    n.append(c)

for i in n:
    if i != 0:
       z.append(i)
if len(z) != 0:
    print(min(z))
else:
print("Ничего нет")
"""
# 3. Определить среднее арифметическое элементов оканчивающихся на тройку
"""
a = [1, 2, 3, 4, 13]
tmp = []
q = 0
for c in a:
    if str(c).endswith('3'):
        tmp.append(c)
if len(tmp) == 0: print("В списке нету чисел, оканчивающихся на тройку");exit(0)

for i in tmp:
    q += i

print(q / len(tmp))
"""
# 4. Определить имеется ли в списке чётный элемент
"""
a = [1, 3]
b = [2, 5]
for c in a:
    if c % 2 == 0:
        print("Имеется чётный элемент")
        exit(0)
        
print("В списке нет чётного элемента")
"""
# 5 Выдать количество нечётных элементов расположенных между минимальным и максимального элементов в списке
"""
a = [19, 0, 2, 4, 5, 3, 20]
c = 0
if a.index(max(a)) > a.index(min(a)):
    for i in range(a.index(min(a)), a.index(max(a))):
        if a[i] % 2 != 0:
            c += 1

if a.index(max(a)) < a.index(min(a)):
    for i in range(a.index(max(a)), a.index(min(a))):
        if a[i] % 2 != 0:
            c += 1

print(c)
"""