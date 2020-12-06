#!python

with open('6.txt') as input:
    g = [h.rstrip() for h in input]
    ##print(g)
    count = 0
    nl = []
    il = []
    l = []

    for i in g:
        if i == '':
            il.append(l)
            l = []
            continue

        l.append(i)
        #print(l)

    il.append(l)

    for e in il:
        d = {}
        for r in e:
            for l in 'abcdefghijklmnopqrstuvwxyz':
                if l in r:
                    if d.get(l) == None:
                        d[l] = 1
                    else:
                        d[l] = d[l] + 1
            ##print(f'r is {r} and d is {d}')
        for m in d:
            if d.get(m) == len(e):
                count += 1
                ##print(m)

        nl.append(count)
        count = 0

    total = 0
    for n in nl:
        total += n

    print(total)
