import re

with open('5.input') as f:
    lines = f.readlines()

    max_stack = 0


    for line in lines:
        if line == '\n':
            break

        if line.startswith('['):
            max_stack = len(line) // 4

    stacks = [ [] for _ in range(max_stack) ]

    for line in lines:
        if line == '\n':
            break


        if '[' in line:
            stack = 0
            for crate in line[1::4]:

                if crate != ' ':
                    stacks[stack].append(crate)
                stack+=1

    for stack in stacks:
        stack.reverse()

    print(stacks)

    for line in lines:
        if line.startswith('move'):
            moves = re.findall('[0-9]+', line)
            moves = list(map(int, moves))
            print(line)

            num_crates = moves[0]
            stack_from = stacks[moves[1]-1]
            stack_to = stacks[moves[2] - 1]
            crates = stack_from[-num_crates:]
            print(crates)
            stack_to.extend(crates)
            stacks[moves[1]-1] = stack_from[:-num_crates]
            print(stacks)

    print('moo')
    output = ''
    for stack in stacks:

        output += stack[-1][0]

    print(output)

    # PLNSSGMFN is wrong