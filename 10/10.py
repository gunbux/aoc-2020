#!python3

with open('10.txt') as input:
    l = [int(g.rstrip()) for g in input]
    l.append(0)
    #print(l)
    l.sort()
    mtd = ojd=tjd = 0
    #print(f'l is {l}')

    print(f'ojd is {ojd} and tjd is {tjd}')
    for n in enumerate(l):
        if n[0] + 1 < len(l):
            #print(f'currently at {n}')
            d = l[n[0]+1]-l[n[0]]
            if d == 1:
                ojd += 1
                #print(f'ojd count is now {ojd}')
            elif d == 3:
                tjd += 1
                #print(f'tjd count is now {tjd}')
            elif d == 2:
                mtd += 1

    tjd += 1
    print(f'ojd is {ojd}, mtd is {mtd} and tjd is {tjd} and the final answer is {ojd * tjd}')
