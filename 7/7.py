#!python
with open('7.txt') as input:
    hasGold = []
    noGold = []
    bbl = {}

    def containsGold(bag):
        print(f'checking {bag} for gold')
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

    print(hasGold)
    print(len(hasGold))

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
