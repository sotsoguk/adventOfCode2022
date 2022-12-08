import os
import time

import timeit






def main():
    # input
    print(os.getcwd())
    day = "08"
    year = "2022"
    debug = False
    input_file = f'../inputs/day{day}{"_debug" if debug else ""}.txt'
    print(input_file)
    part1, part2 = 0, 0
    with open(input_file) as f:
        lines = f.read().splitlines()

    start_time = time.time()
    rows = len(lines)
    cols = len(lines[0])
    visible = [[0 for _ in range(cols)] for _ in range(rows)]
    # scenic = [[0 for _ in range(cols)] for _ in range(rows)]
    grid = [list(map(int,[x for x in row])) for row in lines]
    # 1 left
    # 2 right
    # 4 top
    # 8 bottom
    # left
    for y in range(rows):
        row_max = -1
        for x in range(cols):
            if grid[y][x] > row_max:
                visible[y][x] += 1
                row_max = max(grid[y][x],row_max)
    # right
    for y in range(rows):
        row_max = -1
        for x in range(cols-1,-1,-1):
            if grid[y][x] > row_max:
                visible[y][x] += 2
                row_max = max(grid[y][x],row_max)
    # top
    for x in range(cols):
        col_max = -1
        for y in range(rows):
            if grid[y][x] > col_max:
                visible[y][x] += 4
                col_max = max(grid[y][x],col_max)
    
    # bottom
    for x in range(cols):
        col_max = -1
        for y in range(cols-1,-1,-1):
            if grid[y][x] > col_max:
                visible[y][x] += 8
                col_max = max(grid[y][x],col_max)
    

    #part 1
    for y in range(rows):
        for x in range(cols):
            part1 += 1 if visible[y][x]>0 else 0
    
    # part 2
    part2 = 0
    for y in range(1,rows-1):
        for x in range(1,cols-1):
            score = 1
            #left
            if visible[y][x] & 1 > 0:
                score *= (x)
            else:
                lscore = 1
                for i in range(x-1,-1,-1):
                    if grid[y][i] >= grid[y][x]:
                        break
                    lscore +=1
                score *= lscore
            #right
            if visible[y][x] & 2 > 0:
                score *= (cols-1-x)
            else:
                rscore = 1
                for i in range(x+1,cols):
                    if grid[y][i] >= grid[y][x]:
                        break
                    rscore +=1
                score *= rscore
            #top
            if visible[y][x] & 4 > 0:
                score *= (y)
            else:
                tscore = 1
                for i in range(y-1,-1,-1):
                    if grid[i][x] >= grid[y][x]:
                        break
                    tscore +=1
                score *= tscore
            #bottom
            if visible[y][x] & 8 > 0:
                score *= (rows-1-y)
            else:
                bscore = 1
                for i in range(y+1,rows):
                    if grid[i][x] >= grid[y][x]:
                        break
                    bscore +=1
                score *= bscore
            # scenic[y][x] =score
            part2 = max(part2,score)
    duration = int((time.time() - start_time) * 1000000)
    # for y in scenic:
    #     print(y)
    
    header = "#" * 21

    print(
        f"{header}\n* AoC {year} - Day {day} *\n{header}\n\nPart 1:\t{part1}\nPart 2:\t{part2}\nTime:\t{duration // 1000} ms")


if __name__ == "__main__":
    main()
