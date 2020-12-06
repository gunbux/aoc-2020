#!python

with open('6.txt') as input:
    g = [h.rstrip() for h in input]
    ##print(g)
    p = ''
    count = 0
    nl = []
    il = []

    for i in g:
        if i == '':
            il.append(p)
            p = ''
            continue

        p += i
        #print(p)

    il.append(p)

    for e in il:
        for l in 'abcdefghijklmnopqrstuvwxyz':
            if l in e:
                count += 1

        nl.append(count)
        count = 0
    total = 0
    for n in nl:
        total += n

    print(total)
