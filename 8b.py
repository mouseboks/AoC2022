
class Tree:
    def __init__(self, height):
        self.height = height
        self.scenic_score = -1

    def __repr__(self):
        return str(self.height)


trees = []

def calculate_scenic_score(y, x):
    current_tree = trees[y][x]
    right_score = 0
    left_score = 0
    down_score = 0
    up_score = 0

    for right in range(x+1, len(trees[0])):
        if trees[y][right].height >= current_tree.height:
            right_score += 1
            break
        right_score += 1

    for left in range(x-1, -1, -1):
        if trees[y][left].height >= current_tree.height:
            left_score += 1
            break
        left_score += 1

    for down in range(y+1, len(trees)):
        if trees[down][x].height >= current_tree.height:
            down_score += 1
            break
        down_score += 1

    for up in range(y-1, -1, -1):
        if trees[up][x].height >= current_tree.height:
            up_score += 1
            break
        up_score += 1

    return right_score * left_score * up_score * down_score


def calculate_max_scenic_score(trees):
    max_scenic_score = 0

    for x in range(len(trees[0])):
        for y in range(len(trees)):
            scenic_score = calculate_scenic_score(y,x)
            if scenic_score > max_scenic_score:
                max_scenic_score = scenic_score

    return max_scenic_score

with open('8.input') as f:
    lines = f.readlines()

for line in lines:
    treeline = []
    for char in line.strip():
        treeline.append(Tree(int(char)))
    trees.append(treeline)



print(calculate_max_scenic_score(trees))

# 214032 is too low