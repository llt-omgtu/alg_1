p = 1
for i in range(int(input("Количество элементов: "))):
    if num := int(input(f"Элемент номер {i + 1}: ")) %  5 == 0:
        p *= num

if p == 1:
    print("Элементов нет")
else:
    print(p)