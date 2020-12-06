#!python

with open('5.txt') as input:
    g = [h for h in input]
    r = 128
    c = 8
    id = []

    for i in g:
        f = i[:7]
        b = i[7:]
        l1 = 0
        l2 = 0
        h1 = r
        h2 = c
        cr = 0
        cc = 0

        for m in f:
            if m == 'B':
                l1 = (h1+l1)/2
            if m == 'F':
                h1 = (h1+l1)/2
        cr = l1
        for n in b:
            if n == 'R':
                l2 = (h2+l2)/2
            if n == 'L':
                h2 = (h2+l2)/2
        cc = l2
        #print(f'cr is {cr} and cc is {cc} and id is {cr*8 + cc}')

        id.append(cr*8 + cc)
    id.sort()
    print(id[-1])

    for c in range(int(id[-1])):
        if c not in id:
            if c-1 in id and c+1 in id:
                print(c)
