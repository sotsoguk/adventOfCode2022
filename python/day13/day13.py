import os
import time
from string import ascii_lowercase
from collections import deque
from copy import deepcopy
from sys import maxsize
from ast import literal_eval

    
class Packet():
    def __init__(self, val):
        self.val = val
    
    def __repr__(self) -> str:
        return str(self.val)

    def __lt__(self, rhs):
        # two ints
        if isinstance(self.val,int) and isinstance(rhs.val,int):
            if self.val < rhs.val:
                return True
            if self.val > rhs.val:
                return False
        
        # left int, right list
        if isinstance(self.val,int) and isinstance(rhs.val,list):
            tmp_packet = Packet([self.val])
            return tmp_packet < rhs
        if isinstance(self.val,list) and isinstance(rhs.val,int):
            tmp_packet = Packet([rhs.val])
            return self < tmp_packet
        
        # both lists
        if isinstance(self.val,list) and isinstance(rhs.val,list):
            for v in zip(self.val,rhs.val):
                if v[0] == v[1]:
                    continue
                return Packet(v[0]) < Packet(v[1])
        
        return len(self.val) < len(rhs.val)


def main():
    # input
    print(os.getcwd())
    day = "13"
    year = "2022"
    debug = False
    input_file = f'../inputs/day{day}{"_debug" if debug else ""}.txt'
    print(input_file)
    part1, part2 = 0, 0
    with open(input_file) as f:
        lines = f.read().split('\n\n')

    start_time = time.time()
    
    # parse input
    
    duration = int((time.time() - start_time) * 1000000)
    pairs = []
    all_packets = []
    for block in lines:
        packet1, packet2 = block.splitlines()
        pairs.append((Packet(literal_eval(packet1)),Packet(literal_eval(packet2))))
        all_packets.append(Packet(literal_eval(packet1)))
        all_packets.append(Packet(literal_eval(packet2)))

    
    for i,p in enumerate(pairs,start=1):
        if p[0] < p[1]:
            part1 += i
    # part 2
    divider_two = Packet(literal_eval("[[2]]"))
    divider_six = Packet(literal_eval("[[6]]"))
    all_packets.append(divider_two)
    all_packets.append(divider_six)
    sorted_packets = sorted(all_packets)
    part2 = (sorted_packets.index(divider_two)+1)*(sorted_packets.index(divider_six)+1)
    idx1 = sorted_packets.index(divider_two)+1
    idx2 = sorted_packets.index(divider_six)+1
    print(idx1,idx2)
    header = "#" * 21
    print(
        f"{header}\n* AoC {year} - Day {day} *\n{header}\n\nPart 1:\t{part1}\nPart 2:\t{part2}\nTime:\t{duration // 1000} ms")
    # for p in sorted_packets:
    #     print(p)

if __name__ == "__main__":
    main()
