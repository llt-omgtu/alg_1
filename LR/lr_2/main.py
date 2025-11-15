nums = []


def in
while True:
    try:
        num = int(input("Введите число (0 для окончания ввода): "))
        if num == 0:
            break
        nums.append(num)
    except ValueError:
        print("Некорректный ввод. Пожалуйста, введите целое число.")
        continue


# 1. Все ли элементы положительные
all_pos = all(num > 0 for num in nums)
print(f"1. Все ли элементы положительные: {all_pos}")

count_mult_3 = 0
for num in nums:
    l_digit = abs(num) % 10
    if l_digit % 3 == 0:
        count_mult_3 += 1
print(f"2. Количество элементов, оканчивающихся на цифру, кратную 3: {count_mult_3}")

# 3. Второй максимальный элемент
if len(nums) < 2:
    print("3. Недостаточно элементов для определения второго максимального.")
else:
    uniq_sorted_nums = sorted(list(set(nums)), reverse=True)
    if len(uniq_sorted_nums) < 2:
        print("3. Недостаточно уникальных элементов для определения второго максимального.")
    else:
        sec_max = uniq_sorted_nums[1]
        print(f"3. Второй максимальный элемент: {sec_max}")

# 4. Произведение элементов, которые оканчиваются на 1 и положительные
prod_pos_ends_1 = 1
found_pos_ends_1 = False
for num in nums:
    if num > 0 and num % 10 == 1:
        prod_pos_ends_1 *= num
        found_pos_ends_1 = True
if found_pos_ends_1:
    print(f"4. Произведение элементов, оканчивающихся на 1 и положительных: {prod_pos_ends_1}")
else:
    print("4. Нет положительных элементов, оканчивающихся на 1.")
