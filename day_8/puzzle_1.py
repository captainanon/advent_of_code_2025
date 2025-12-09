from time import perf_counter
from math import sqrt, prod
from collections import defaultdict

def solve(input):
    with open(input) as file:
        input = [tuple(map(int, x.split(','))) for x in file.read().split('\n')]
    
    distances, circuits, connections, top_circuits = [], defaultdict(set), 1000, 3
    
    for i, jnct_1 in enumerate(input[:-1]):
        distances += [(sqrt((jnct_1[0] - jnct_2[0])**2 + (jnct_1[1] - jnct_2[1])**2 + (jnct_1[2] - jnct_2[2])**2), jnct_1, jnct_2) for jnct_2 in input[i + 1:]]
    
    sorted_distances = sorted(distances)
    for distance in sorted_distances[:connections]:
        jnct_1, jnct_2, exists, idx_1, idx_2 = distance[1], distance[2], 0, 0, 0
        for num, circuit in circuits.items():
            if jnct_1 in circuit:
                idx_1 = num
                exists = 1
            if jnct_2 in circuit:
                idx_2 = num
                exists = 1
            if idx_1 and idx_2:
                break

        if exists and idx_1 and idx_2 and idx_1 != idx_2:
            circuits[idx_1].update(circuits[idx_2])
            del circuits[idx_2]
        elif exists and idx_1:
            circuits[idx_1].add(jnct_2)
        elif exists and idx_2:
            circuits[idx_2].add(jnct_1)
        elif not exists:
            max_ = 0 if len(circuits) == 0 else max(circuits.keys())
            circuits[max_ + 1].add(jnct_1)
            circuits[max_ + 1].add(jnct_2)
            
    return prod(sorted([len(v) for v in circuits.values() if len(v) != 0], reverse=True)[:top_circuits])

if __name__ == '__main__':
    start_time = perf_counter()
    answer = solve('day_8/input.txt')
    runtime = round(perf_counter() - start_time, 3)
    print('answer =', answer) # 140008
    print('runtime =', runtime, 's') # 0.568 s