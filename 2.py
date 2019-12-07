

def run(d):
    p = 0
    while 1:
        if d[p] == 1:
            a, b, x = d[p+1:p+4]
            d[x] = d[a] + d[b]
            p += 4
        elif d[p] == 2:
            a, b, x = d[p+1:p+4]
            d[x] = d[a] * d[b]
            p += 4
        elif d[p] == 99:
            return d[0]
        else:
            return None


def task1(d):
    d[1] = 12
    d[2] = 2
    print(run(d))


def task2(d):
    for i in range(0, 100):
        for j in range(0, 100):

            d_copy = d[:]
            d_copy[1] = i
            d_copy[2] = j

            out = run(d_copy)

            if out != 19690720:
                continue

            print(i, j)
            return


if __name__ == '__main__':
    d = list(map(int, input().strip().split(',')))

    # task1(d)
    task2(d)
