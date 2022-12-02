import os
import time


def solve_part1(input):
    calc_score = lambda a,b : (((b-a)%-3)+3)%3
    score = 0
    for (a, b) in input:
        score += b+(3+calc_score(a,b)*3)%9
        # score += b
        # # determine outcome
        # if a == b:
        #     # draw
        #     score += 3
        # elif b == (a % 3)+1:
        #     score += 6

    return score


def solve_part2(input):
    score = 0
    for (a, b) in input:
        if b == 2:  # draw
            score += (3+a)
        elif b == 3:  # win
            score += (6 + (a % 3) + 1)
        else:  # lose
            score += (a+1) % 3+1
    return score


def main():
    # input
    print(os.getcwd())
    day = "02"
    year = "2022"
    input_file = f'../inputs/day{day}.txt'
    print(input_file)
    part1, part2 = 0, 0
    with open(input_file) as f:
        lines = f.read().splitlines()

    # parse input
    opponent_shape = {'A': 1, 'B': 2, 'C': 3}
    player_shape = {'X': 1, 'Y': 2, 'Z': 3}
    games = []
    for l in lines:
        a, b = l.split(' ')
        games.append((opponent_shape[a], player_shape[b]))
    start_time = time.time()
    print(solve_part1(games))
    print(solve_part2(games))

    # part1 & 2

    duration = int((time.time() - start_time) * 1000000)

    header = "#" * 20
    print(
        f"{header}\n*AoC {year} - Day {day} *\n{header}\n\nPart 1:\t{part1}\nPart 2:\t{part2}\nTime:\t{duration // 1000} ms")


if __name__ == "__main__":
    main()
