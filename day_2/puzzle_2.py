import textwrap
from time import time

def solve(input):
    with open(input) as file:
        input = [(int(y[0]), int(y[1])) for y in [x.split('-') for x in file.read().split(',')]]
    s = set()
    for r in input:
        for n in range(r[0], r[1] + 1):
            if n in s:
                continue
            st = str(n)
            l = len(st)
            for i in range(l - 1, 0, -1):
                if int(l) % i != 0:
                    continue
                lst = list(map(int, textwrap.wrap(st, i)))
                if len(set(lst)) == 1:
                    s.add(n)
                    break
    return sum(s)
if __name__ == '__main__':
  input = 'day_2/input.txt'
  t0 = time()
  print('answer =', solve(input)) # 25912654282
  print('runtime =', time() - t0, 's')