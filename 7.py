class TreeNode:

    def __init__(self, name, isdir, parent=None, size=0):
        self.name = name
        self.isdir = isdir
        self.parent = parent
        self.size = size
        self.children = set()



    # A sample method
    def get_child_with_name(self, name):
        for child in self.children:
            if child.name == name:
                return child
        return None

    def get_total_size(self):
        total_size = self.size
        for child in self.children:
            total_size += child.get_total_size()
        return total_size

    def __repr__(self):
        return self.name

    def __lt__(self, other):
        self.name < other.name

def getSize(node):
    return node.get_total_size()

def get_dirs_size_less(dir: TreeNode, size):
    dirs = []
    for child in dir.children:
        print('children: ' + str(child))
        if child.isdir:
            dir_size=get_dirs_size_less(child, size)
            print('dir_size: ' + str(dir_size))
            dirs.extend(dir_size)
    if dir.get_total_size() <= size:
        dirs.append(dir)


    return dirs



root_dir = TreeNode(name='/', isdir=True)
current_dir = root_dir

with open('7.input') as f:
    lines = f.readlines()

    linenum = 0

    line = ''

    while linenum < len(lines):

        if(line == '$ BREAK'):
            break

        line = lines[linenum].strip()

        if line.startswith('$ cd /'):
            current_dir = root_dir
        elif line.startswith('$ ls'):
            linenum += 1
            line = lines[linenum].strip()

            while not line.startswith('$'):
                if line.startswith('dir'):
                    dirname = line.split(' ')[1]
                    if not current_dir.get_child_with_name(dirname):
                        child_dir = TreeNode(name=dirname, isdir=True, parent=current_dir)
                        current_dir.children.add(child_dir)
                else:
                    child_file = TreeNode(name=line.split(' ')[1], isdir=False, size=int(line.split(' ')[0]))
                    current_dir.children.add(child_file)
                linenum+=1
                if linenum < len(lines):
                    line = lines[linenum].strip()
                else:
                    line = '$ BREAK'
            linenum -= 1
        elif line.startswith('$ cd ..'):
            current_dir = current_dir.parent
        elif line.startswith('$ cd'):
            current_dir = current_dir.get_child_with_name(line.split(' ')[2])

        linenum+=1

    print('root size' + str(root_dir.get_total_size()))
    dirs = get_dirs_size_less(root_dir, 100000000)


    dirs.sort(key=getSize)

    print('free space: ' + str(70000000 - root_dir.get_total_size()))

    needed_space = 30000000 - (70000000 - root_dir.get_total_size())

    print('needed space:' + str(needed_space))
    for dir in dirs:
        if dir.get_total_size() >= needed_space:
            print(dir.get_total_size())
            break