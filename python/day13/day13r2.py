data = [[eval(t[0]),eval(t[1])] for t in [s.split('\n') for s in open("../inputs/day13.txt").read().split('\n\n')]]

# return -1 if l < r, +1 if l > r, and 0 otherwise
def compare(l,r):
    #print("L:",l,"\nR:",r,"\n\n") # for debugging
    if type(l) is int and type(r) is int:
        if l < r: return -1
        if l > r: return +1
        else:     return 0

    if type(l) is int: l = [l]
    if type(r) is int: r = [r]

    if l == [] and r != []: return -1
    if l != [] and r == []: return +1
    if l == [] and r == []: return 0

    tf = compare(l[0],r[0])
    if tf:
        return tf
    else:
        return compare(l[1:],r[1:])

rightorder = [i for i in range(1,len(data)+1) if compare(data[i-1][0],data[i-1][1]) == -1]
print("PART 1: Sum of right indices: ", sum(rightorder))

#### PART 2 ####

import functools
data = [eval(t) for t in open("../inputs/day13.txt").read().split()] + [[[2]]] + [[[6]]]
data.sort(key=functools.cmp_to_key(compare))
print("PART 2: Decoder key: ", (1 + data.index([[2]])) * (1 + data.index([[6]])))