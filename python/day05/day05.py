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

    def run_command_9000(command, stack_set):
        (num, source, dest) = command
        for i in range(num):
            stack_set[dest-1].append(stack_set[source-1].pop())

    def run_command_9001(command, stack_set):
        (num, source, dest) = command
        stack_set[dest-1].extend(stack_set[source-1][-num:])
        del stack_set[source-1][len(stack_set[source-1])-num:]

    for c in commands:
        run_command_9000(c, stacks)
        run_command_9001(c, stacks2)

    # create ouput
    part1 = ''.join([s.pop() for s in stacks])
    part2 = ''.join([s.pop() for s in stacks2])

    duration = int((time.time() - start_time) * 1000000)
    header = "#" * 21
    print(
        f"{header}\n* AoC {year} - Day {day} *\n{header}\n\nPart 1:\t{part1}\nPart 2:\t{part2}\nTime:\t{duration // 1000} ms")


if __name__ == "__main__":
    main()
