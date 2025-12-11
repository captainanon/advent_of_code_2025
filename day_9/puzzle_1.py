from time import perf_counter

def solve(input):
    with open(input) as file:
        input = [tuple(map(int, x.split(','))) for x in file.read().split('\n')]

    corners = []   
    for i, corner_1 in enumerate(input):
        for corner_2 in input[i + 1:]:
            corners.append((corner_1, corner_2))
    
    areas = []
    for corner_1, corner_2 in corners:
        area = abs(corner_1[0] - corner_2[0] + 1) * abs(corner_1[1] - corner_2[1] + 1)
        areas.append(area)
    
    answer = max(areas)
            
    return answer

if __name__ == '__main__':
    start_time = perf_counter()
    answer = solve('day_9/input.txt')
    runtime = round(perf_counter() - start_time, 3)
    print('answer =', answer) # 4782151432
    print('runtime =', runtime, 's') # 0.091 s