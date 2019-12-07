
def run(d, inp):
    p = 0
    while 1:
        instr = d[p] % 100
        ia = d[p] // 100 % 10
        ib = d[p] // 1000 % 10
        ix = d[p] // 10000 % 10

        if instr == 1:
            # ADD
            a, b, x = d[p+1:p+4]
            if ix:
                print('Error: invalid instr %d: output not in position mode!' % d[p])
                return None
            d[x] = (a if ia else d[a]) + (b if ib else d[b])
            p += 4
        elif instr == 2:
            # MUL
            a, b, x = d[p+1:p+4]
            if ix:
                print('Error: invalid instr %d: output not in position mode!' % d[p])
                return None
            d[x] = (a if ia else d[a]) * (b if ib else d[b])
            p += 4

        elif instr == 3:
            # INPUT
            dst = d[p+1]
            if ia:
                print('Error: invalid instr %d: dest not in position mode!' % d[p])
                return None
            print('INPUT [%d] -> %d' % (inp, dst))
            d[dst] = inp
            p += 2
        elif instr == 4:
            # OUTPUT
            src = d[p+1]
            print('OUTPUT <- %d' % (src if ia else d[src]))
            p += 2

        elif instr == 5:
            # JT
            test, jmp = d[p+1], d[p+2]
            if (test if ia else d[test]) != 0:
                p = jmp if ib else d[jmp]
            else:
                p += 3
        elif instr == 6:
            # JF
            test, jmp = d[p+1], d[p+2]
            if (test if ia else d[test]) == 0:
                p = jmp if ib else d[jmp]
            else:
                p += 3

        elif instr == 7:
            # LT
            a, b, x = d[p+1:p+4]
            if ix:
                print('Error: invalid instr %d: output not in position mode!' % d[p])
                return None
            d[x] = 1 if (a if ia else d[a]) < (b if ib else d[b]) else 0
            p += 4
        elif instr == 8:
            # EQ
            a, b, x = d[p+1:p+4]
            if ix:
                print('Error: invalid instr %d: output not in position mode!' % d[p])
                return None
            d[x] = 1 if (a if ia else d[a]) == (b if ib else d[b]) else 0
            p += 4

        elif d[p] % 100 == 99:
            return d[0]
        else:
            print('Unknown instruction %d' % d[p])
            return None

def task1(d):
    run(d, 1)

def task2(d):
    run(d, 5)

if __name__ == '__main__':
    d = list(map(int, input().strip().split(',')))

    # task1(d)
    task2(d)
