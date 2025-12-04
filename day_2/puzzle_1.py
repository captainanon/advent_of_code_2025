from time import time

def solve(input):
    with open(input) as file:
        input = [(int(y[0]), int(y[1])) for y in [x.split('-') for x in file.read().split(',')]]
    s = 0
    for r in input:
            for n in range(r[0], r[1] + 1):
                st = str(n)
                mid = len(st) // 2
                if st[0:mid] == st[mid:]:
                     s += n
    return s
if __name__ == '__main__':
    input = 'day_2/input.txt'
    t0 = time()
    print('answer =', solve(input)) # 19574776074
    print('runtime =', time() - t0, 's') # 0.5422699451446533 s