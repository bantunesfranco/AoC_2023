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
    

def spin(rounded, cube):
    global grid
    rounded = tilt_north(rounded)
    grid = tuple(map("".join, zip(*make_grid(rounded, cube, grid))))
    for _ in range(2):
        rounded = tilt_north(rounded)
        grid = tuple(map("".join, zip(*make_grid(rounded, cube, grid)[::-1])))
    rounded = tilt_north(rounded)
    return tuple(map("".join, zip(*make_grid(rounded, cube, grid)[::-1])))

grid = tuple(lines)
grids = {grid}
iter = 0

for i in range(1, 1000000000):

    spin(rounded, cube)
    for l in grid:
        print(l)
    if grid in grids:
        break
    print(i)
    grids.add(grid)

res = 0
for j, line in enumerate(grid):
    res += line.count("O") * (len(grid) - j)

print(f"Part 2 output = {res}")
    