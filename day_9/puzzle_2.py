from time import perf_counter

def solve(input):
    with open(input) as file:
        vertices = [tuple(map(int, x.split(','))) for x in file.read().split('\n')]

    corners = []   
    for i, corner_1 in enumerate(vertices):
        for corner_2 in vertices[i + 1:]:
            corners.append((corner_1, corner_2))

    edges = []
    for i in range(len(vertices)):
        v1 = vertices[i]
        v2 = vertices[(i + 1) % len(vertices)] 
        edges.append((v1, v2))

    areas = []
    for corner_1, corner_2 in corners:
        if is_valid_rectangle(corner_1, corner_2, edges):
            x1, y1 = corner_1
            x2, y2 = corner_2
            x_min, x_max = sorted([x1, x2])
            y_min, y_max = sorted([y1, y2])
            area = (x_max - x_min + 1) * (y_max - y_min + 1)
            areas.append(area)

    answer = max(areas)
            
    return answer

def is_valid_rectangle(corner_1, corner_2, edges):
    cx1, cy1 = corner_1
    cx2, cy2 = corner_2
    cx_min, cx_max = sorted([cx1, cx2])
    cy_min, cy_max = sorted([cy1, cy2])

    for edge_1, edge_2 in edges:
        ex1, ey1 = edge_1
        ex2, ey2 = edge_2
        ex_min, ex_max = sorted([ex1, ex2])
        ey_min, ey_max = sorted([ey1, ey2])
        if (
            ex_max > cx_min
            and  ex_min < cx_max
            and  ey_max >  cy_min
            and  ey_min < cy_max
        ):
            return False 
            
    return True

if __name__ == '__main__':
    start_time = perf_counter()
    answer = solve('day_9/input.txt')
    runtime = round(perf_counter() - start_time, 3)
    print('answer =', answer) # 1450414119
    print('runtime =', runtime, 's') # 14.641 s