import random


def generate_maze(width, height):
    maze = [[3] * width for _ in range(height)]

    def carve_passages_from(cx, cy, maze):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(directions)
        for (dx, dy) in directions:
            nx, ny = cx + 2 * dx, cy + 2 * dy
            if 0 <= nx < width and 0 <= ny < height and maze[ny][nx] == 3:
                maze[cy + dy][cx + dx] = 0
                maze[ny][nx] = 0
                carve_passages_from(nx, ny, maze)

    start_x, start_y = 0, 0
    maze[start_y][start_x] = 1
    carve_passages_from(start_x, start_y, maze)

    # Поиск случайной точки выхода, достижимой из начальной точки
    possible_exits = [(x, y) for x in range(width) for y in range(height) if maze[y][x] == 0]
    end_x, end_y = random.choice(possible_exits)
    maze[end_y][end_x] = 2

    return maze, (end_y, end_x)


def print_maze(maze):
    symbols = {3: '3', 1: '1', 2: '2', 0: ' '}
    for row in maze:
        print("".join([symbols[cell] for cell in row]))

