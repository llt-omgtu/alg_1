from collections import Counter

def process_list(lst, m):
    n = len(lst)

    # Наибольшую сумму цепочки из m элементов
    max_chain = max(sum(lst[i:i + m]) for i in range(n - m + 1))
    print("Наибольшая сумма цепочки из m элементов:", max_chain)

    # Частота появления каждого элемента
    freq = Counter(lst)
    print("Частоты элементов:", dict(freq))

    # Определить элементы встречающиеся 1 раз
    unique_elems = [k for k, v in freq.items() if v == 1]
    print("Уникальные элементы:", unique_elems)

    # Определить наибольшую сумму из элементов
    max_current = max_global = lst[0]
    for num in lst[1:]:
        max_current = max(num, max_current + num)
        max_global = max(max_global, max_current)
    print("Наибольшая сумма подмассива:", max_global)

lst = [1, -2, 3, 10, -5, 6]
m = 3
process_list(lst, m)