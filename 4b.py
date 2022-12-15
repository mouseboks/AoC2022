with open('4.input') as f:
    lines = f.readlines()

    inrange = 0
    for line in lines:
        line = line.strip()

        range1=list(map(int,line.split(',')[0].split('-')))
        range2 = list(map(int,line.split(',')[1].split('-')))

        if range1[0]>range2[1]:
            continue
        if range1[1]<range2[0]:
            continue
        inrange+=1

    print(inrange)

# 915 is too high
