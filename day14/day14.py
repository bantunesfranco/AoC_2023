with open("test.txt") as f:
    lines = f.read().splitlines()

# Part 1
rounded = [(x, y) for y, line in enumerate(lines) for x, c in enumerate(line) if c == "O"]
cube = [(x, y) for y, line in enumerate(lines) for x, c in enumerate(line) if c == "#"]
rounded.sort()

nround = []
print(rounded)
for (x, y) in rounded:
    i = y
    while i >= 0:
        if y == 0:
           print(x, i)
           nround.append((x, i))
           break
        if lines[i][x] == "#": #or ((x, i)) in nround():
            print(x, i)
            nround.append((x, i + 1))
            break
        i -= 1
    print()
print(nround)

grid = []
for y, line in enumerate(lines):
    new = []
    for x, c in enumerate(line):
        if (x,y) in nround:
            new.append("O")
        elif (x,y) in cube:
            new.append("#")
        else:
            new.append(".")
    grid.append(new)

for l in grid:
    print(l)