# 1. На вход подаются 3 списка, необходимо определить элементы, с помощью которых составлены списки,
#    найти множество пересечений и объединений списков
#    (пересечение - только повторяющиеся (между 12, 23, 13), объединение - все (без повторов) (между 12, 23, 13, 123))

def uniq(aa: list, bb: list):
    for i in aa:
        if i in bb:
            return i
    return 'Нету'

a = [1,2,3,3]
b = [1,5,5,6]
c = [7,7,8,2, 1]

print(f"a -> b => {uniq(a, b)} => {set(a + b)}")
print(f"a -> c => {uniq(a, c)} => {set(a + c)} ")
print(f"b -> c => {uniq(b, c)} => {set(b + c)} ")
print(f"a -> b -> c => {uniq(a, [uniq(b,c)])} => {set(a + b + c)}")

# 2. На вход подается строка, определить символы, которые не встречаются в строке (только латинские буквы с учетом регистра)

ascii_ = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
s = 'ewrwee fdfefdf erfd1'
a = []
for i in ascii_:
    if i not in s:
        a.append(i)

print(a)

# 3. На вход подается список из положительных целых чисел, определить цифры десятичной системы счисления, в которых нет ни в одном числе

a = [123, 42, 53, 12]
b = []
s = ""
digit = "0123456789"
for i in a:
    s += str(i)

for i in digit:
    if i not in s:
        b.append(i)
print(b)
