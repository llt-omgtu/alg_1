nums = []


while True:
    num = int(input("Введите число (0 для окончания ввода): "))
    if num == 0:
        break
    nums.append(num)


# 1. Все ли элементы положительные
print(all(num > 0 for num in nums))

count = 0
for num in nums:
    l_digit = abs(num) % 10
    if l_digit % 3 == 0:
        count += 1
print(count)

# 3. Второй максимальный элемент
if len(nums) < 2:
    print("Надо больше элементов")
else:
    uniq = sorted(list(set(nums)), reverse=True)
    if len(uniq) < 2:
        print("Надо больше уникальных элементов")
    else:
        sec_max = uniq[1]
        print(sec_max)

# 4. Произведение элементов, которые оканчиваются на 1 и положительные
pos = 1
flag = False
for num in nums:
    if num > 0 and num % 10 == 1:
        pos *= num
        flag = True
if flag:
    print(pos)
else:
    print("Нет положительных элементов")
