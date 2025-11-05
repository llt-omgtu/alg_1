# 1. Определить сумму отрицательный элементов
sum = 0
for i in range(int(input("Количество элементов: "))):
    num =+ int(input(f"Элемент номер {i + 1}: "))
    if num < 0:
        sum += num
        
print(sum)
# 2. Определить минимальное значение среди положительных элементов
min_z = None
for i in range(int(input("Количество элементов: "))):
    num = + int(input(f"Элемент номер {i + 1}: "))
    if min_z is None or min_z > num:
        min_z = num

print(min_z)
# 3. Определить образует ли элементы равномерно убывающие последовательность
razn = None
tmp = None
for i in range(int(input("Количество элементов: "))):
    num = + int(input(f"Элемент номер {i + 1}: "))
    if tmp is None:
        tmp = num
        continue
        
    if razn is None:
        razn = tmp - num
        continue
        
    if razn != tmp - num:
        print("Последовательность убывает не равномерно!")
        exit(0)
        
print("Последовательность равномерна")
# 4. Определить количество локальных минимумов

n = int(input("Количество элементов: "))
if n < 3:
    print("Надо больше 3 элементов")
else:
    count = 0

    a = int(input("Элемент номер 1: "))
    b = int(input("Элемент номер 2: "))

    for i in range(2, n):
        c = int(input(f"Элемент номер {i + 1}: "))

        if a > b and b < c:
            count += 1
            print(b)
    a, b = b, c
print(f"Кол-во локальных переменных: {count}")


# 5. Определить второй минимальный элемент

min_z = None
min_a = None
for i in range(int(input("Количество элементов: "))):
    num = + int(input(f"Элемент номер {i + 1}: "))
    if min_z is None or min_z > num:
        min_a = min_z
        min_z = num
        
    if min_a is None:
        min_a = min_z

print(min_a)


