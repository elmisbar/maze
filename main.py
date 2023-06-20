import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import random


def generate_maze_pdf(maze, filename):
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.imshow(maze, cmap='binary')

    with PdfPages(filename) as pdf:
        pdf.savefig(fig)


def generate_maze(width, height):
    maze = [[1] * width for _ in range(height)]

    start_x = random.randint(0, width - 1)
    start_y = random.randint(0, height - 1)
    maze[start_y][start_x] = 0

    directions = [(0, -2), (0, 2), (-2, 0), (2, 0)]

    def is_valid(x, y):
        return 0 <= x < width and 0 <= y < height and maze[y][x] == 1

    def make_path(x, y, dx, dy):
        maze[y + dy // 2][x + dx // 2] = 0
        maze[y + dy][x + dx] = 0

    def generate(x, y):
        random.shuffle(directions)
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if is_valid(new_x, new_y):
                make_path(x, y, dx, dy)
                generate(new_x, new_y)

    generate(start_x, start_y)
    return maze


maze = generate_maze(50, 50)
generate_maze_pdf(maze, "maze.pdf")
