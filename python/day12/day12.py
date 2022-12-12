import os
import time
from string import ascii_lowercase
from collections import deque
from copy import deepcopy
from sys import maxsize


def find_shortest_path(start, goal, grid):
    rows, cols = len(grid), len(grid[0])

    def get_neighbours(pos):
        possible_positions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        positions = []
        for p in possible_positions:
            possible_x = pos[0] + p[0]
            possible_y = pos[1] + p[1]
            if (possible_x >= 0 and possible_x < cols and possible_y >= 0 and possible_y < rows):
                positions.append((possible_x, possible_y))
        return positions

    grid[start[1]][start[0]] = (1, 0)
    queue = deque()
    queue.append(start)

    while len(queue) > 0:
        curr_pos = queue.popleft()
        curr_x, curr_y = curr_pos[0], curr_pos[1]
        curr_height, curr_steps = grid[curr_y][curr_x]
        possible_neighbors = get_neighbours(curr_pos)

        for n in possible_neighbors:
            to_height, to_steps = grid[n[1]][n[0]]
            if to_steps >= 0 and to_steps <= (curr_steps + 1):
                continue
            elif to_height <= curr_height + 1:
                grid[n[1]][n[0]] = (to_height, curr_steps+1)
                queue.append(n)
    return grid[goal[1]][goal[0]][1]


def main():
    # input
    print(os.getcwd())
    day = "12"
    year = "2022"
    debug = False
    input_file = f'../inputs/day{day}{"_debug" if debug else ""}.txt'
    print(input_file)
    part1, part2 = 0, 0
    with open(input_file) as f:
        lines = f.read().splitlines()

    start_time = time.time()
    rows, cols = len(lines), len(lines[0])

    # def get_neighbours(pos):
    #     possible_n = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    #     neighs = []
    #     for pn in possible_n:
    #         xp = pos[0] + pn[0]
    #         yp = pos[1] + pn[1]
    #         if (xp >= 0 and xp < cols and yp >= 0 and yp < rows):
    #             neighs.append((xp, yp))
    #     return neighs
    start, goal = (0, 0), (0, 0)
    start_points = []
    grid = [[(0, -1) for _ in range(cols)] for _ in range(rows)]
    for y, row in enumerate(lines):
        for x, e in enumerate(row):
            if e == 'S':
                start = (x, y)
                grid[y][x] = (1, -1)
            elif e == 'E':
                goal = (x, y)
                grid[y][x] = (26, -1)
            else:
                grid[y][x] = (ascii_lowercase.index(e)+1, -1)
            if e == 'a':
                start_points.append((x, y))
    start_points.append(start)

    part1 = find_shortest_path(start_points[-1], goal, deepcopy(grid))
    # steps = []
    # for sp in start_points:
    #     steps.append(find_shortest_path(sp, goal, deepcopy(grid)))
    # part2 = min([s for s in steps if s > 0]) # filter out impossible positions

    duration = int((time.time() - start_time) * 1000000)

    header = "#" * 21
    print(
        f"{header}\n* AoC {year} - Day {day} *\n{header}\n\nPart 1:\t{part1}\nPart 2:\t{part2}\nTime:\t{duration // 1000} ms")


if __name__ == "__main__":
    main()
