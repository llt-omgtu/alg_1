"""
for i in range(int(input())):
    q1 = str(input()).split(' ')
    q2 = str(input()).split(' ')
    s11 = int(q1[0]) * int(q1[1]) * int(q1[2]) / 1000  # * int(q1[6])
    s12 = int(q1[3]) * int(q1[4]) * int(q1[5]) / 1000  # * int(q1[7])
    print(s11, s12)
"""
import os
for a in range(len(os.listdir('./inputs'))):
    with open(f'./inputs/{os.listdir('./inputs')[a]}', 'r') as f:
        n = int(f.readline().strip())
        firms = []
        for _ in range(n):
            data = f.readline().split()
            x1, y1, z1 = int(data[0]), int(data[1]), int(data[2])
            x2, y2, z2 = int(data[3]), int(data[4]), int(data[5])
            c1, c2 = float(data[6]), float(data[7])
            firms.append(((x1, y1, z1, c1), (x2, y2, z2, c2)))

    comp = None
    cost = float('inf')

    for idx, (p1, p2) in enumerate(firms, start=1):
        x1, y1, z1, c1 = p1
        x2, y2, z2, c2 = p2

        S1 = 2 * (x1 * y1 + x1 * z1 + y1 * z1)
        S2 = 2 * (x2 * y2 + x2 * z2 + y2 * z2)

        det = (x1 * y1 * z1) * S2 - (x2 * y2 * z2) * S1
        if det == 0:
            continue

        milk = (1000 * (c1 * S2 - c2 * S1)) / det

        if milk < cost:
            cost = milk
            comp = idx

    print(f"{comp} {cost:.2f} ==== {os.listdir('./inputs')[a]}")

print(f"========================OUTPUT======================================")
for a in range(len(os.listdir('./outputs'))):
    with open(f'./outputs/{os.listdir('./outputs')[a]}', 'r') as f:
        print(f"{f.readline()} ==== {os.listdir('./outputs')[a]}")