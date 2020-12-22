#!python3
count = 0
def dfs(pointer,remaining):
    global count
    #print(f'pointer at {pointer} and remaining is {remaining}')
    if remaining == [] and pointer == l[-1]:
        count += 1
        print(f'count is currently {count}')
        pass
    else:
        if pointer in remaining:
            remaining.remove(pointer)
        o = sd[pointer]
        for c in o:
            if c in remaining:
                rl = remaining[:]
                rl.remove(c)
                dfs(c,rl)
    pass

with open('10.txt') as input:
    l = [int(g.rstrip()) for g in input]
    l.append(0)
    #print(l)
    l.sort()
    l.append(l[-1]+3)
    ojd=tjd = 0
    sd = {}
    #print(f'l is {l}')
    remaining = l[:]

    print(f'ojd is {ojd} and tjd is {tjd}')
    for n in enumerate(l):
        nl = []
        for i in range(-3,4):
            if i == 0:
                continue
            else:
                if n[1]+i in l:
                    nl.append(n[1]+i)
        sd[n[1]] = nl

    dfs(0,remaining)
    print(f'count is {count}')
