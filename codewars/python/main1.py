# 1
"""
words = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
def smash(words):
    return " ".join(words)
print(smash(words))
"""
# 2
"""
def solution(text: str, ending):
    if text.endswith(ending):
        return True
    else:
        return False
"""
"""
def solution(text, ending):
    return text.endswith(ending)
"""
# 3
"""
def likes(names):
    long = len(names)
    if long == 0:
         return "no one likes this"
    elif long == 1:
        return f"{names[0]} likes this"
    elif long == 2:
        return f"{names[0]} and {names[1]} like this"
    elif long == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    elif long >= 4:
        return f"{names[0]}, {names[1]} and {long-2} others like this"

print(likes([]))
print(likes(["a", "b"]))
"""
"""
def likes(names: list[str]) -> str:
    match len(names):
        case 0: return f'no one likes this'
        case 1: return f'{names[0]} likes this'
        case 2: return f'{names[0]} and {names[1]} like this'
        case 3: return f'{names[0]}, {names[1]} and {names[2]} like this'
        case _: return f'{names[0]}, {names[1]} and {len(names) - 2} others like this'
"""
# 5
"""

"""

"""
def get_sum(a,b):
    return sum(range(min(a, b), max(a, b) + 1))
    """
# 6
"""
def accum(st):
    string = []
    for i in range(len(st)):
        string.append(f"{st[i].upper()}{(st[i] * i).lower()}")
    return '-'.join(string)
"""

"""
def accum(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))
"""

# 7
"""
def find_short(s):
    tmp = float("inf")
    for i in s.split():
        if len(i) < tmp:
            tmp = len(i)
    return int(tmp)
"""

"""
def find_short(s):
    return min(len(i) for i in s.split())
"""
# 8
"""
def cointBits(n):
    return sum(map(int, bin(n)[2:]))
"""
"""
from string import ascii_uppercase
def validate_euro(serial_number):
    tmp =  int(sum(map(int, serial_number[2:])))
    print(tmp)
    tmp += ascii_uppercase.index(serial_number[1]) + ascii_uppercase.index(serial_number[0]) + 2
    print(tmp, ascii_uppercase.index(serial_number[1]) + ascii_uppercase.index(serial_number[0]) + 2, sum(map(int, str(tmp))))
    while len(str(tmp)) != 0:
        tmp = sum(map(int, str(tmp)))
    return tmp == 7
    """