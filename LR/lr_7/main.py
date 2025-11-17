# 1. Определить кол-во слов с чётной длинной
"""
a = 'awer 12 asd 2222 dddd'

c = 0

for i in a.strip().split():
    if len(i) % 2 == 0:
        c += 1

print(c)
"""

# 2. Определить кол-во чётных чисел
"""
a = 'qw2eqwe1233 dsd1 2 4 11 ww'
c = 0
for i in a:
    if not i.isdecimal():
        a = a.replace(i, ' ', 1)

for i in a.strip().split():
    if int(i) % 2 == 0:
        c += 1

print(c)
"""

# 3. Заменить в строке все слова палиндромы (читается туда и обратно одинаково)
"""
a = 'Шалаш  шалаши  шалаш твав  дед'.lower()
q = a.strip().split()
for i in range(len(q)):
    if q[i] == q[i][::-1].lower():
        q.pop(i)
        q.insert(i, '11')

print(" ".join(q))
"""

# 4. В строке определить наибольшую цепочку из одинаковых символов
strok = 'aaaabbbwwwaaaaa'

c = 0
tmp = strok[0]

s = {}
for i in strok:
    if tmp == i:
        c += 1
    else:
        c += 1
        s.update({c: tmp * c})

        tmp = i
        c = 0

s.update({c: tmp * (c + 1)})
print(max(s.keys()), s.get(max(s.keys())))









