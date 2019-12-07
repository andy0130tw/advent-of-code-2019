


def task1(d1, d2):
    cnt = 0
    for i in range(d1, d2+1):
        s = str(i)
        has_double = False
        prev = chr(ord('0')-1)
        ok = True
        for c in s:
            if c == prev:
                has_double = True
            elif c < prev:
                ok = False
                break
            prev = c

        if ok and has_double:
            cnt += 1

    print(cnt)


def task2(d1, d2):
    cnt = 0
    for i in range(d1, d2+1):
        s = str(i)
        has_exactly_double = False
        streak = 0
        prev = chr(ord('0')-1)
        ok = True
        for c in s:
            if c == prev:
                streak += 1
            else:
                if streak == 1:
                    has_exactly_double = True
                streak = 0

                if c < prev:
                    ok = False
                    break
            prev = c

        if streak == 1:
            has_exactly_double = True

        if ok and has_exactly_double:
            cnt += 1
            print(i)

    print(cnt)

if __name__ == '__main__':
    d1, d2 = map(int, input().strip().split('-'))

    # task1(d1, d2)
    task2(d1, d2)
