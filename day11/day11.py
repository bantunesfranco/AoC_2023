with open("input.txt") as f:
    lines = f.read().splitlines()

def insert (src, s, pos):
    return src[:pos] + s + src[pos:]


## part 1
space = []
for line in lines:
    space.append(line)
    if all(c == "." for c in line):
        space.append(line)

newspace = []
add = 0
size = len(space[0])
for x in range(size):
    col = [line[x+add] for line in space]
    if all(c == "." for c in col):
        add += 1
        for y in range(len(space)):
            space[y] = insert(space[y], ".", x+add)


galaxies = set()
for y, line in enumerate(space):
    for x, char in enumerate(line):
        if char == "#":
            galaxies.add((x, y))

galaxies = list(galaxies)
res = []
for i, (x1, y1) in enumerate(galaxies):
    for (x2, y2) in galaxies[i+1:]:
        res.append(abs(x2-x1) + abs(y2-y1))

print(f"part 1 output = {sum(res)}")

## part 2
space = []
for line in lines:
    space.append(line)
    if all(c == "." for c in line):
        for i in range(1000000):
            space.append(line)

newspace = []
add = 0
size = len(space[0])
for x in range(size):
    col = [line[x+add] for line in space]
    if all(c == "." for c in col):
        add += 1
        for y in range(len(space)):
            space[y] = insert(space[y], ".", x+add)


galaxies = set()
for y, line in enumerate(space):
    for x, char in enumerate(line):
        if char == "#":
            galaxies.add((x, y))

galaxies = list(galaxies)
res = []
for i, (x1, y1) in enumerate(galaxies):
    for (x2, y2) in galaxies[i+1:]:
        res.append(abs(x2-x1) + abs(y2-y1))

print(f"part 1 output = {sum(res)}")