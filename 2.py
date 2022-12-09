
with open('2.input') as f:
    lines = f.readlines()

    score = 0

    # Rock == A
    # Paper == B
    # Scissors = C

    # X = lose
    # y = draw
    # z = win

    for line in lines:
        line = line.strip()
        match line:
            case 'A X':
                score += 3
            case 'A Y':
                score += 4
            case 'A Z':
                score += 8
            case 'B X':
                score += 1
            case 'B Y':
                score += 5
            case 'B Z':
                score += 9
            case 'C X':
                score += 2
            case 'C Y':
                score += 6
            case 'C Z':
                score += 7

    print(score)
