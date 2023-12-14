with open("input.txt") as f:
    lines = f.read().splitlines()

rounded = [(x, y) for y, line in enumerate(lines) for x, c in enumerate(line) if c == "O"]
cube = [(x, y) for y, line in enumerate(lines) for x, c in enumerate(line) if c == "#"]

def make_grid(rounded, cube, lines):
    grid = []
    for y, line in enumerate(lines):
        new = ""
        for x, c in enumerate(line):
            if (x,y) in rounded:
                new += "O"
            elif (x,y) in cube:
                new += "#"
            else:
                new += "."
        grid.append(new)
    return grid

def tilt_north(rounded):
    rounded.sort(key=lambda x: (x[0], x[1]))
    nrounded = []
    for (x, y) in rounded:
        i = y
        while i >= 0:
            if i == 0:
                nrounded.append((x, i))
                break
            if (lines[i - 1][x] == "#"):
                nrounded.append((x, i))
                break
            if (x, i - 1) in nrounded:
                nrounded.append((x, i))
                break
            i -= 1
    return list(set(nrounded))

# Part 1

nrounded = tilt_north(rounded)
grid = make_grid(nrounded, cube, lines)

res = 0
for i, line in enumerate(grid):
    res += line.count("O") * (len(grid) - i)

print(f"Part 1 output = {res}")

## Part 2
    
def tilt_south(rounded):
    rounded.sort(key=lambda x: (x[0], x[1]), reverse=True)
    nrounded = []
    for (x, y) in rounded:
        i = y
        while i < len(lines):
            if i == len(lines) - 1:
                nrounded.append((x, i))
                break
            if (lines[i + 1][x] == "#"):
                nrounded.append((x, i))
                break
            if (x, i + 1) in nrounded:
                nrounded.append((x, i))
                break
            i += 1
    return list(set(nrounded))

def tilt_east(rounded):
    rounded.sort(key=lambda x: (x[1], x[0]), reverse=True)
    nrounded = []
    for (x, y) in rounded:
        i = x
        while i <= len(lines[y]):
            if i == len(lines[y]) - 1:
                nrounded.append((i, y))
                break
            if (lines[y][i + 1] == "#"):
                nrounded.append((i, y))
                break
            if (i + 1, y) in nrounded:
                nrounded.append((i, y))
                break
            i += 1
    return list(set(nrounded))

def tilt_west(rounded):
    rounded.sort(key=lambda x: (x[1], x[0]))
    nrounded = []
    for (x, y) in rounded:
        i = x
        while i >= 0:
            if i == 0:
                nrounded.append((i, y))
                break
            if (lines[y][i - 1] == "#"):
                nrounded.append((i, y))
                break
            if (i - 1, y) in nrounded:
                nrounded.append((i, y))
                break
            i -= 1
    return list(set(nrounded))

grid = lines
grids = []
while True:

    rounded = tilt_north(rounded)
    grid = make_grid(rounded, cube, grid)

    rounded = tilt_west(rounded)
    grid = make_grid(rounded, cube, grid)

    rounded = tilt_south(rounded)
    grid = make_grid(rounded, cube, grid)

    rounded = tilt_east(rounded)
    grid = make_grid(rounded, cube, grid)

    res = 0
    for j, line in enumerate(grid):
        res += line.count("O") * (len(grid) - j)

    print(res)
    if grid in grids:
        break

    grids.append(grid)

print(res)