#!python

with open('3.txt') as input:
    map = [g.rstrip() for g in input]
    #print(map)
    def main(a,b):
        count = 0
        pointer = [0,0]
        while pointer[1] <= len(map)-1:
            if pointer[0] >= len(map[0]):
                pointer[0] = pointer[0] % len(map[0])
            if map[pointer[1]][pointer[0]] == '#':
                count += 1
            pointer = [pointer[0]+a,pointer[1]+b]
        return count

    x = main(1,1)
    y = main(3,1)
    z = main(5,1)
    p = main(7,1)
    n = main(1,2)
    print(x*y*z*p*n)
