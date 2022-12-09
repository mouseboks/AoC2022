with open('3.input') as f:
    lines = f.readlines()

    totalpriority = 0

    for line in lines:
        line = line.strip()

        set1 = set(line[:len(line)//2])
        set2 = set(line[len(line)//2:])

        print(set1.intersection(set2))
        priority = 0
        for char in list(set1.intersection(set2)):

            if char.isupper():
                priority += ord(char)-38
            else:
                priority += ord(char)-96

        totalpriority += priority

    print(totalpriority)

