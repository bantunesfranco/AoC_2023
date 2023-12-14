with open("input.txt") as f:
	start_grid = tuple(f.read().splitlines())

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

grid = start_grid
tilt()

res = sum(row.count("O")*(len(grid)-i) for i, row in enumerate(grid))
print(f"Part 1 output = {res}")


# Part 2

def tilt():
	global grid
	for _ in range(4):
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

		grid = tuple(row[::-1] for row in grid)

i = 0
grid = start_grid
grids = [grid]
while True:

	i += 1
	tilt()

	if grid in grids:
		break
	
	grids.append(grid)

j = grids.index(grid)

grid = grids[(1000000000-j) % (i - j) + j]
res = sum(row.count("O")*(len(grid)-i) for i, row in enumerate(grid))

print(f"Part 2 output = {res}")
