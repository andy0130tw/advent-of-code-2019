

dmap = {
    'U': (0, 1),
    'D': (0, -1),
    'L': (-1, 0),
    'R': (1, 0),
}

def task1(d1, d2):
    pts = set()
    cx, cy = 0, 0
    for s in d1:
        c = s[0]
        n = int(s[1:])
        dx, dy = dmap[c]
        for _ in range(n):
            cx += dx
            cy += dy
            pts.add((cx, cy))

    ints = set()
    cx, cy = 0, 0
    for s in d2:
        c = s[0]
        n = int(s[1:])
        dx, dy = dmap[c]
        for _ in range(n):
            cx += dx
            cy += dy
            if (cx, cy) in pts:
                ints.add((cx, cy))

    print(min(map(lambda z: abs(z[0]) + abs(z[1]), ints)))


def task2(d1, d2):
    pts = {}
    cx, cy = 0, 0
    step = 0
    for s in d1:
        c = s[0]
        n = int(s[1:])
        dx, dy = dmap[c]
        for _ in range(n):
            cx += dx
            cy += dy
            step += 1
            pts[(cx, cy)] = step

    ints = {}
    cx, cy = 0, 0
    step = 0
    for s in d2:
        c = s[0]
        n = int(s[1:])
        dx, dy = dmap[c]
        for _ in range(n):
            cx += dx
            cy += dy
            step += 1
            if (cx, cy) in pts:
                ints[(cx, cy)] = step + pts[(cx, cy)]

    print(min(ints.values()))


if __name__ == '__main__':
    d1 = input().strip().split(',')
    d2 = input().strip().split(',')

    # task1(d1, d2)
    task2(d1, d2)
