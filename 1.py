
with open('1.input') as f:
    lines = f.readlines()

    calorie_list = []
    calories = 0

    for line in lines:
        if line == '\n':
            calorie_list.append(calories)
            calories = 0
        else:
            calories = calories + int(line)

    calorie_list.sort(reverse=True)

    print(sum(calorie_list[0:3]))

