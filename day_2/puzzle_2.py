from time import time

def solve(input):
    with open(input) as file:
        input = [(int(y[0]), int(y[1])) for y in [x.split('-') for x in file.read().split(',')]]
    s = 0
    for r in input:
        for n in range(r[0], r[1] + 1):
            st = str(n)
            l = len(st)
            for m in range(1, l // 2 + 1):
                if l % m != 0:
                    continue
                b = st[:m]
                if b * (l // m) == st:
                    s += n
                    break
    return s
if __name__ == '__main__':
    input = 'day_2/input.txt'
    t0 = time()
    print('answer =', solve(input)) # 25912654282
    print('runtime =', time() - t0, 's') # 1.6090972423553467 s