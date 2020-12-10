#!python
with open('7.txt') as input:
    hasGold = []
    bbl = []
    class bag(object):
        def __init__(self,baglist):
            self.baglist = baglist

        def getBaglist(self):
            return self.baglist

    def containsGold(bag):
        if bag in hasGold:
            return True
        else:
            if bag == None:
                return False
            for i in bag.getBagList():
                if containsGold(i):
                    hasGold.append(i)
                    return True

    for g in input:
        h = g.rstrip()[:-1].split(' contain ')
        b = h[1].split(',')
        if b == 'no other bags':
            b = None


