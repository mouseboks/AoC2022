with open('4.input') as f:
    lines = f.readlines()

    inrange = 0
    for line in lines:
        line = line.strip()

        range1=list(map(int,line.split(',')[0].split('-')))
        range2 = list(map(int,line.split(',')[1].split('-')))

        print(line)
        #range2 is in range1
        if(range1[0]<=range2[0] and range1[1]>=range2[1]):
            inrange+=1
            print('yes')
        # range1 is in range2
        elif(range2[0]<=range1[0] and range2[1]>=range1[1]):
            inrange+=1
            print('yes')
        else:
            print('no')

    print(inrange)


# 567 answer is wrong