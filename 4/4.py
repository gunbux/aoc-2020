def validate(i):
    if int(i.get('byr')) > 2002 or int(i.get('byr')) < 1920:
        return False
    if int(i.get('iyr')) > 2020 or int(i.get('iyr')) < 2010:
        return False
    if int(i.get('eyr')) > 2030 or int(i.get('eyr')) < 2020:
        return False
    if 'cm' in i.get('hgt') or 'in' in i.get('hgt'):
        if 'cm' in i.get('hgt'):
            h = i.get('hgt')
            h = int(h.replace('cm',''))
            if h < 150 or h > 193:
                return False
        if 'in' in i.get('hgt'):
            h = i.get('hgt')
            h = int(h.replace('in',''))
            if h < 59 or h > 76:
                return False
    else:
        return False
    if i.get('hcl')[0] == '#':
        for m in i.get('hcl')[1:]:
            if m not in '0123456789abcdef':
                return False
    else:
        return False
    el = ['amb','blu','brn','gry','grn','hzl','oth']
    if i.get('ecl') not in el:
        return False
    if len(i.get('pid')) == 9:
        for m in i.get('pid'):
            if m not in '0123456789':
                return False
    else:
        return False
    return True
with open('4.txt') as input:
    count = 0
    pl = []
    p = {}
    l = [g.rstrip() for g in input]

    #print(l)
    for i in l:
        if i == '':
            pl.append(p)
            p = {}
            continue

        e = i.split()
        for r in e:
            t = r.split(':')
            p[t[0]] = t[1]
    pl.append(p)

    for h in pl:
        #print(h)
        #print(f'length of h is {len(h)}')
        ##Part 2 solution
        if len(h) == 8:
            if validate(h):
                count += 1
                #print('valid')
        elif len(h) == 7 and h.get('cid') == None:
            if validate(h):
                count += 1
                #print('valid')

##Part 1 Solution
##        if len(h) == 8:
##            count += 1
##        elif len(h) == 7 and h.get('cid') == None:
##            count += 1

    print(count)
