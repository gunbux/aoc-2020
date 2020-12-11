#!python
with open('7.txt') as input:
    hasGold = []
    noGold = []
    bbl = {}
    c = {}

    def containsGold(bag):
        ##print(f'checking {bag} for gold')
        if bbl[bag] == None or bag == None:
            noGold.append(bag)
            return False
        else:
            if bag in hasGold:
                return True
            elif bag in noGold:
                return False
            elif bag == 'shiny gold':
                return True
            for i in bbl[bag]:
                if containsGold(i):
                    ##print('gold found')
#                    if i not in hasGold and i != 'shiny gold':
#                        hasGold.append(i)
                    hasGold.append(bag)
                    return True
                else:
                    noGold.append(i)

    def countbags(bag):
        bc = 0
        l = bbl[bag]
        ##print(f'counting bags: {bag}')
        ##print(f'dp list is {c}')
        if l == None:
            if bag not in c:
                c[bag] = 0
            return 0
        if bag in c:
            return c[bag]
        else:
            for i in l:
                ##print(f'i is {i} and l is {l}')
                bc += l[i]
                y = l[i]
                bc += y*countbags(i)
            if bag not in c:
                c[bag] = bc
            return bc

    for g in input:
        h = g.rstrip()[:-1].split(' contain ')
        a = h[0].replace(' bags','')
        b = h[1].split(', ')
        o = {}
        for n in b:
            if n == 'no other bags':
                o = None
                continue
            n = n.replace(' bags','')
            n = n.replace(' bag','')
            o[n[2:]] = int(n[0])
        bbl[a] = o


    for v in bbl:
        ##print(f'searching for bag {v}')
        containsGold(v)

    print(countbags('shiny gold'))

# Potato Code
#    class bag(object):
#        def __init__(self,name,baglist):
#            self.baglist = baglist
#            self.name = name
#
#        def getBaglist(self):
#            return self.baglist
#
#        def getName(self):
#            return self.name
#
#        def __str__(self):
#            return f'{self.name} bag contains {str(self.baglist)}'
#
#    def containsGold(bag):
#        if bag in hasGold:
#            return True
#        else:
#            if bag == None:
#                return False
#            for i in bag.getBaglist():
#                if containsGold(i):
#                    hasGold.append(i)
#                    return True
