def p1(lop):
    for n in range(len(lop)):
        for b in range(1,len(lop[n+1:])+1):
            #print(f'n is {lop[n]} and b is {lop[n+b]} and cn is {cn}')
            if lop[n] + lop[b+n] == cn:
                #print('number found')
                return True
    #print('number not found')
    return False

with open('9.txt') as input:
    g = [int(h.rstrip()) for h in input]
    #print(g)

    for i in enumerate(g):
        #print(i)
        #print(f'currently at {i}')
        if i[0] <= 25:
            continue
        else:
            ix = i[0]
            cn = i[1]
            ulop = []
            for m in range(ix-25,ix):
                ulop.append(g[m])

            lop = ulop[:]
            lop.sort()

            #print(f'lop is {lop}')
            if p1(lop) == False:
                en = i[1]
                print(f'lop is {lop} and ulop is {ulop}')
                print(f'number found. number is {i[1]}')
                break

    # Part 2
    i = 0
    while True:
        if i > len(g):
            break
        r = 0
        while True:
            if r >= len(g):
                break
            sol = [g[r]]
            #print(f'i is {i} and u is {u}')
            for y in range(r+1,1+r+i):
                #print(f'y is {y}')
                if y < len(g) -1:
                    sol.append(g[y])

            #print(f'sol is {sol} and sum is {sum(sol)}')
            if sum(sol) == en and len(sol) != 1:
                print(sol)
                break
            r += 1
        i += 1

    print(sol)
#    for i in range(len(g)):
#        for u in enumerate(g):
#            sol = [u[1]]
#            #print(f'i is {i} and u is {u}')
#            for y in range(u[0]+1,1+u[0]+i):
#                #print(f'y is {y}')
#                if y < 25:
#                    sol.append(g[y])
#
#            print(f'sol is {sol} and sum is {sum(sol)}')
#            if sum(sol) == en and len(sol) != 1:
#                print(sol)
#                break
#            elif sum(sol) > en:
#                for a in range(u[0],len(g)):
#                    g.pop(a)
