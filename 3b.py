with open('3.input') as f:
    lines = f.readlines()

    totalpriority = 0

    for i in range(0, len(lines), 3):
        line1 = lines[i].strip()
        line2 = lines[i+1].strip()
        line3 = lines[i + 2].strip()

        set1 = set(line1)
        set2 = set(line2)
        set3 = set(line3)

        print(set1.intersection(set2).intersection(set3))
        priority = 0
        for char in list(set1.intersection(set2).intersection(set3)):

            if char.isupper():
                priority += ord(char)-38
            else:
                priority += ord(char)-96

        totalpriority += priority

    print(totalpriority)

