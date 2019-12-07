


def task1():
    c = 0

    while 1:
        try:
            x = int(input())
        except EOFError:
            break

        c += x // 3 - 2
    return c

def task2():
    c = 0

    while 1:
        try:
            x = int(input())
        except EOFError:
            break

        while x >= 6:
            x = x // 3 - 2
            c += x
    return c

if __name__ == '__main__':
    # task1()
    task2()
    print(c)
