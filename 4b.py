with open('4.input') as f:
    lines = f.readlines()

    inrange = 0
    for line in lines:
        line = line.strip()

        range1=list(map(int,line.split(',')[0].split('-')))
        range2 = list(map(int,line.split(',')[1].split('-')))

        print(line)
        #range2 is in range1

        if range1[0]>range2[1]:
            print('no')
            continue
        if range1[1]<range2[0]:
            print('no')
            continue
        inrange+=1
        print('yes')

    print(inrange)

# 915 is too high
