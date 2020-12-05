#! python

with open('2.txt') as input:
    count = 0
    for i in input:
        ##print(i) #- Working
        i = i.rstrip()
        x = i.split(': ')
        print(x) #- Working
        k = x[0].split(' ')
        n = k[0].split('-')
        print(f'n is {n}')
        print(f'k is {k}')
        if x[1][int(n[0])-1] == k[1] and x[1][int(n[1])-1] == k[1]:
            continue
        elif x[1][int(n[0])-1] == k[1] or x[1][int(n[1])-1] == k[1]:
            count += 1
    print(count)
