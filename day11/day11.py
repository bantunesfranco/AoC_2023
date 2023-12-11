with open("test.txt") as f:
    lines = f.read().splitlines()

def insert (src, s, pos):
    return src[:pos] + s + src[pos:]

space = []
for line in lines:
    space.append(line)
    if all(c == "." for c in line):
        space.append(line)

y = 0
newspace = []
add = 0
for x in range(len(space[0])+1):
    if add == 1:
        add = 0
        continue
    col = [line[x] for line in space]
    if all(c == "." for c in col):
        add = 1
        for y in range(len(space)):
            space[y] = insert(space[y], ".", x)


galaxies = set()
for y, line in enumerate(space):
    for x, char in enumerate(line):
        if char == "#":
            galaxies.add((x, y))

galaxies = list(galaxies)
for l in galaxies[:-1]:
    g = galaxies.pop()
    print(galaxies)