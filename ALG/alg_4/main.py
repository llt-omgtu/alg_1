from os import listdir

def rotate(axis, k, s, x, y, z, n):
    if axis == 'X' and x == k:
        if s == 1:
            y, z = z, n + 1 - y
        else:
            y, z = n + 1 - z, y
    elif axis == 'Y' and y == k:
        if s == 1:
            x, z = z, n + 1 - x
        else:
            x, z = n + 1 - z, x
    elif axis == 'Z' and z == k:
        if s == 1:
            x, y = y, n + 1 - x
        else:
            x, y = n + 1 - y, x
    return x, y, z

for filename in sorted(listdir('Кубик Рубика')):
    if filename.startswith('input_s1_') and filename.endswith('.txt'):

        with open(f"{'Кубик Рубика'}\\{filename}", 'r') as f:
            n, m = map(int, f.readline().split())
            x, y, z = map(int, f.readline().split())
            rotations = [line.strip().split() for line in f.readlines()]

        for axis, k, s in rotations:
            x, y, z = rotate(axis, int(k), int(s), x, y, z, n)

        with open(f"{'Кубик Рубика'}\\{filename.replace('input', 'output')}", 'r') as f:
            output = f.read().strip()

        print(f"Файл: {filename}")
        print(f"Финальные коорды: {x} {y} {z}")
        print(f"Правильные коорды: {output}")
        print("-" * 20)