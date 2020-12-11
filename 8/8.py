#!python
with open('8.txt') as input:
    g = [h for h in input]
    for m in enumerate(g):
        r = g[:]
        il = []
        pointer = 0
        a = 0

        if m[1][0:3] == 'nop':
            r[m[0]] = m[1].replace('nop','jmp')
        elif m[1][0:3] == 'jmp':
            r[m[0]] = m[1].replace('jmp','nop')
        else:
            continue

        while True:
            #print(f'pointer is currently at position {pointer}')
            if pointer == len(r):
                print(f'terminated succesfully. acc is at {a}')
                break
            if pointer in il:
                break
            il.append(pointer)
            i = r[pointer].rstrip().split()
            if i[0] == 'acc':
                if i[1][0] == '+':
                    a += int(i[1][1:])
                elif i[1][0] == '-':
                    a -= int(i[1][1:])
            if i[0] == 'jmp':
                if i[1][0] == '+':
                    pointer += int(i[1][1:])
                    continue
                if i[1][0] == '-':
                    pointer -= int(i[1][1:])
                    continue
            pointer += 1

    print(a)
