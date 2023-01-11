import sys
import numpy as np

def main () -> None:

    last = lambda in_list: in_list[len(in_list) - 1]

    itxt = open("../inputs/day09.txt", mode='r').read().split()
    move = [(d, int(s)) for d, s in zip(itxt[::2], itxt[1::2])]
    dirs = {    'R': np.array([1, 0]), 'L': np.array([-1, 0]), 
                'U': np.array([0, 1]), 'D': np.array([0, -1]) }
    
    rope = [ [ np.array([0, 0]) ] for i in range(10) ]
    
    def domove(i):
        if i == len(rope):
            return
        
        dif = last(rope[i-1]) - last(rope[i])
        
        if      last(rope[i-1])[0] != last(rope[i])[0] \
            and last(rope[i-1])[1] != last(rope[i])[1] \
            and (abs(dif[0]) > 1 or abs(dif[1]) > 1):
            if dif[0] > 0 and dif[1] > 0:
                rope[i].append(last(rope[i]) + np.array([1,1]))
            elif dif[0] > 0 and dif[1] < 0:
                rope[i].append(last(rope[i]) + np.array([1,-1]))
            elif dif[0] < 0 and dif[1] > 0:
                rope[i].append(last(rope[i]) + np.array([-1,1]))
            elif dif[0] < 0 and dif[1] < 0:
                rope[i].append(last(rope[i]) + np.array([-1,-1]))
        
        elif abs(dif[0]) > 1 or abs(dif[1]) > 1:
            if dif[0] > 0:
                rope[i].append(last(rope[i]) + np.array([1,0]))
            elif dif[0] < 0:
                rope[i].append(last(rope[i]) + np.array([-1,0]))
            elif dif[1] > 0:
                rope[i].append(last(rope[i]) + np.array([0,1]))
            elif dif[1] < 0:
                rope[i].append(last(rope[i]) + np.array([0,-1]))
        
        domove(i+1)
        
    
    for d, s in move:
        for _ in range(s):
            rope[0].append(last(rope[0]) + dirs.get(d))
            
            domove(1)
    
    print(len(set([ (i[0], i[1]) for i in rope[-1]])))

    
if __name__ == '__main__':
    sys.exit(main())