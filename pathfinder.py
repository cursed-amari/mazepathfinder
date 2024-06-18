import heapq
import time
import os

from mazeGenerator import generate_maze


def heuristic(a, b):
    """Манхэттенское расстояние"""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def print_matrix(matrix):
    os.system('cls' if os.name == 'nt' else 'clear')  # Очищает экран
    for row in matrix:
        print(" ".join(str(cell) for cell in row))


def a_star_search(matrix, start, goal):
    """Кратчайший путь в матрице от start до goal с использованием алгоритма A*."""
    rows, cols = len(matrix), len(matrix[0])
    open_list = []
    heapq.heappush(open_list, (0 + heuristic(start, goal), 0, start))
    came_from = {start: None}
    g_score = {start: 0}

    while open_list:
        _, current_cost, current = heapq.heappop(open_list)

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = came_from[current]
            return path[::-1]

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (current[0] + dx, current[1] + dy)
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and matrix[neighbor[0]][neighbor[1]] != 3:
                tentative_g_score = current_cost + 1

                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    g_score[neighbor] = tentative_g_score
                    f_score = tentative_g_score + heuristic(neighbor, goal)
                    heapq.heappush(open_list, (f_score, tentative_g_score, neighbor))
                    came_from[neighbor] = current

    return None  # Если пути не существует


if __name__ == "__main__":
    matrix, finish = generate_maze(45, 27)
    matrix[0][0] = 1
    matrix[finish[0]][finish[1]] = "2"

    start = (0, 0)
    goal = (finish[0], finish[1])

    start_time = time.time()
    path = a_star_search(matrix, start, goal)
    end_time = time.time()
    print(end_time - start_time)

    temp = (3, 2)

    step_path = 0

    if path:
        for step in path:
            time.sleep(0.5)
            matrix[temp[0]][temp[1]] = "0"
            matrix[step[0]][step[1]] = '1'
            temp = step
            step_path += 1
            print_matrix(matrix)
        print("Step = ", step_path)
    else:
        print("Путь не найден.")


