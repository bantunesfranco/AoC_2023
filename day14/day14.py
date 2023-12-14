with open("test.txt") as f:
    grid = tuple(f.read().splitlines())

def tilt():
    global grid
    grid = ["".join(row) for row in zip(*grid)]

    for i, row in enumerate(grid):
        line = ""
        parts = row.split("#")
        for j, p in enumerate(parts):
            line += "O"*p.count("O")
            line += "."*p.count(".")
            if j != len(parts)-1:
                line += "#"
        grid[i] = line
    grid = tuple("".join(row) for row in zip(*grid))


tilt()

res = sum(row.count("O")*(len(grid)-i) for i, row in enumerate(grid))
print(f"Part 1 output = {res}")


# Part 2
