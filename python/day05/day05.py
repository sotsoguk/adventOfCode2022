import os
import time
import re
import copy


def main():
    # input
    print(os.getcwd())
    day = "05"
    year = "2022"
    input_file = f'../inputs/day{day}.txt'
    print(input_file)
    # part1, part2 = 0, 0
    with open(input_file) as f:
        lines = f.read().split('\n\n')

    start_time = time.time()

    # process stack
    num_stacks = int(lines[0][-2].split(' ')[-1])
    stacks = [[] for _ in range(num_stacks)]
    indices = [4*i++1 for i in range(num_stacks)]

    for i in reversed(lines[0].splitlines()[:-1]):
        elems = [i[k] for k in indices]
        for j, e in enumerate(elems):
            if e != ' ':
                stacks[j].append(e)

    stacks2 = copy.deepcopy(stacks)
    # process commands
    commands = [list(map(int, [c.split(' ')[i] for i in [1, 3, 5]]))
                for c in lines[1].splitlines()]

    def run_command(command, stack_set, cargo_9001=False):
        (num, source, dest) = command
        if cargo_9001:
            stack_set[dest-1].extend(stack_set[source-1][-num:])
        else:
            stack_set[dest-1].extend(reversed(stack_set[source-1][-num:]))
        del stack_set[source-1][len(stack_set[source-1])-num:]

    for c in commands:
        run_command(c, stacks)
        run_command(c, stacks2, cargo_9001=True)

    # create ouput
    def create_output(stack_set): return ''.join([s.pop() for s in stack_set])
    part1 = create_output(stacks)
    part2 = create_output(stacks2)

    duration = int((time.time() - start_time) * 1000000)
    header = "#" * 21
    print(
        f"{header}\n* AoC {year} - Day {day} *\n{header}\n\nPart 1:\t{part1}\nPart 2:\t{part2}\nTime:\t{duration // 1000} ms")


if __name__ == "__main__":
    main()
