with open('6.input') as f:
    line = f.read()

    for i in range(len(line)):
        chars = set(line[i:i+14])
        if len(chars) == 14:
            print(i+14)
            break