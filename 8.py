
class Tree:
    def __init__(self, height):
        self.height = height
        self.visible = False

    def __repr__(self):
        return str(self.visible)


trees = []

with open('8.input') as f:
    lines = f.readlines()

for line in lines:
    treeline = []
    for char in line.strip():
        treeline.append(Tree(int(char)))
    trees.append(treeline)

for treerow in trees:
    max_height = -1
    for tree in treerow:
        if tree.height > max_height:
            tree.visible = True
            max_height = tree.height

for treerow in trees:
    max_height = -1
    for tree in reversed(treerow):
        if tree.height > max_height:
            tree.visible = True
            max_height = tree.height

for index in range(len(trees)-1):
    max_height = -1
    for treerow in trees:
        tree = treerow[index]
        if tree.height > max_height:
            tree.visible = True
            max_height = tree.height

for index in range(len(trees[0])):
    max_height = -1
    for treerow in reversed(trees):
        print(len(trees[0])-1-index)
        tree = treerow[len(trees[0])-1-index]
        if tree.height > max_height:
            tree.visible = True
            max_height = tree.height

visible = 0
for treerow in trees:
    for tree in treerow:
        if tree.visible:
            visible += 1

print (visible)