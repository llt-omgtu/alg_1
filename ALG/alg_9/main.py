"""Паук и муха

В комнате, представляющей собой параллелепипед, находятся паук и муха.

Паук и муха располагаются на стенах, полу или потолке.
Определите минимальное расстояние, которое необходимо проползти пауку, чтобы добраться до мухи.
Примечание: ползать паук может, естественно, только по стенам, полу или потолку.
Входной файл
Первая строка содержит три целых числа a, b и c, разделенных пробелами - ширина, глубина и высота комнаты (1  a, b, c  100).
Вторая строка содержит три целых числа Sx, Sy, Sz, разделенных пробелами - координаты паука относительно начала комнаты (0, 0).
Третья строка содержит три целых числа Fx, Fy, Fz, разделенных пробелами - координаты мухи относительно начала комнаты (0, 0).
(0  Sx, Fx  a; 0  Sy, Fy  b; 0  Sz, Fz  c), все координаты лежат на стенах, поле или потолке комнаты.
Выходной файл
Первая строка должна содержать минимальное расстояние, которое необходимо проползти пауку, чтобы добраться до мухи - число с тремя знаками после запятой.
Пример 1 (см. рисунок):
Input.txt
60 14 30
20 0 20
60 7 20
Output.txt
47.000
Пример 2:
Input.txt
60 14 30
20 0 0
60 0 20
Output.txt
44.721
"""

import math
import os

def solve_spider_fly(a, b, c, sx, sy, sz, fx, fy, fz):
    if (sx == fx and (sx == 0 or sx == a)) or (sy == fy and (sy == 0 or sy == b)) or (
            sz == fz and (sz == 0 or sz == c)):
        if sx == fx:
            return math.hypot(sy - fy, sz - fz)
        elif sy == fy:
            return math.hypot(sx - fx, sz - fz)
        else:
            return math.hypot(sx - fx, sy - fy)

    if sy == 0 and fx == a:
        return math.hypot((a - sx) + fy, abs(sz - fz))

    if sy == 0 and fx == 0:
        return math.hypot(sx + (b - fy), abs(sz - fz))

    if sy == b and fx == a:
        return math.hypot((a - sx) + (b - fy), abs(sz - fz))

    if sy == b and fx == 0:
        return math.hypot(sx + fy, abs(sz - fz))

    if sx == 0 and fy == 0:
        return math.hypot(sy + (a - fx), abs(sz - fz))

    if sx == 0 and fy == b:
        return math.hypot((b - sy) + (a - fx), abs(sz - fz))

    if sx == a and fy == 0:
        return math.hypot((b - sy) + fx, abs(sz - fz))

    if sx == a and fy == b:
        return math.hypot(sy + fx, abs(sz - fz))

    if sz == 0 and fz == c:
        return min(
            math.hypot(sx + fx, c + abs(sy - fy)),
            math.hypot((a - sx) + (a - fx), c + abs(sy - fy)),
            math.hypot(sy + fy, c + abs(sx - fx)),
            math.hypot((b - sy) + (b - fy), c + abs(sx - fx))
        )

    if sy == 0 and fz == c:
        return math.hypot(sx + fx, (c - sz) + (c - fz))

    if sy == 0 and fz == 0:
        return math.hypot(sx + fx, sz + fz)

    if sx == a and fz == c:
        return math.hypot((b - sy) + fy, (c - sz) + (c - fz))

    if sx == a and fz == 0:
        return math.hypot((b - sy) + fy, sz + fz)

    candidates = []

    candidates.append(math.hypot(sx + fx, abs(sy - fy)))
    candidates.append(math.hypot(sx + fx, sy + fy))
    candidates.append(math.hypot((a - sx) + (a - fx), abs(sy - fy)))
    candidates.append(math.hypot((a - sx) + (a - fx), sy + fy))

    candidates.append(math.hypot(sy + fy, abs(sx - fx)))
    candidates.append(math.hypot(sy + fy, sx + fx))
    candidates.append(math.hypot((b - sy) + (b - fy), abs(sx - fx)))
    candidates.append(math.hypot((b - sy) + (b - fy), sx + fx))

    candidates.append(math.hypot(sz + fz, abs(sx - fx)))
    candidates.append(math.hypot(sz + fz, sx + fx))
    candidates.append(math.hypot((c - sz) + (c - fz), abs(sx - fx)))
    candidates.append(math.hypot((c - sz) + (c - fz), sx + fx))

    candidates.append(math.hypot(sz + fz, abs(sy - fy)))
    candidates.append(math.hypot(sz + fz, sy + fy))
    candidates.append(math.hypot((c - sz) + (c - fz), abs(sy - fy)))
    candidates.append(math.hypot((c - sz) + (c - fz), sy + fy))

    return min(candidates)

# блядь... помогите... что ты такое




for i in os.listdir('Паук и муха'):
    if i.startswith('input'):
        with open(f'Паук и муха\\{i}') as f:
            a, b, c = f.readline().split(' ')
            sx, sy, sz = f.readline().split(' ')
            fx, fy, fz = f.readline().split(' ')

        result1 = solve_spider_fly(int(a), int(b), int(c), int(sx), int(sy), int(sz), int(fx), int(fy), int(fz))

        with open(f'Паук и муха\\output_s1_{i[-6:-4]}.txt') as fo:
            aa = fo.read()

        with open(f'Паук и муха\\input_s1_{i[-6:-4]}.txt') as fo:
            ab = fo.read()

        if aa == f'{result1:.3f}':
            print(f"PASSED: Файл: {i} | Ответ {result1:.3f}")
        else:
            print(f"ERORR: Файл: {i} | Ответ {result1:.3f} | Верный ответ: {aa} | Данные для ввода: \n{ab}")


