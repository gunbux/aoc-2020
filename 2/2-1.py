#! python

with open('2.txt') as input:
    count = 0
    for i in input:
        ##print(i) #- Working
        i = i.rstrip()
        x = i.split(': ')
        ##print(x) #- Working
        k = x[0].split(' ')
        n = k[0].split('-')
        if x[1].count(k[1]) >= int(n[0]) and x[1].count(k[1]) <= int(n[1]):
            count += 1
    print(count)
