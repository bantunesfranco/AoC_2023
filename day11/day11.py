with open("test.txt") as f:
	lines = f.read().splitlines()

### first try
def insert (src, s, pos):
	return src[:pos] + s + src[pos:]

## part 1
space = []
for line in lines:
	space.append(line)
	if all(c == "." for c in line):
		line="1"*len(line)
		space.append(line)

newspace = []
add = 0
size = len(space[0])
for x in range(size):
	col = [line[x+add] for line in space]
	if all(c == "." or c == "1" for c in col):
		add += 1
		for y in range(len(space)):
			space[y] = insert(space[y], "1", x+add)

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
		line="1"*len(line)
		space.append(line)

newspace = []
add = 0
size = len(space[0])
for x in range(size):
	col = [line[x+add] for line in space]
	if all(c == "." or c == "1" for c in col):
		add += 1
		for y in range(len(space)):
			space[y] = insert(space[y], "1", x+add)

galaxies = set()
addy = 0
for y, line in enumerate(space):
	if all(c == "1" for c in line):
		addy += (1000000 - 2)
	addx = 0
	for x, char in enumerate(line):
		col = [line[x] for line in space]
		if all(c == "1" for c in col):
			addx += (1000000- 2)
		if char == "#":
			galaxies.add((x+addx, y+addy))

galaxies = list(galaxies)
res = []
for i, (x1, y1) in enumerate(galaxies):
	for (x2, y2) in galaxies[i+1:]:
		res.append(abs(x2-x1) + abs(y2-y1))

print(f"part 2 output = {sum(res)}\n")

### new solution
def space_walk(lines, factor) -> int:
	empty_lines = [y for y, line in enumerate(lines) if all(c == "." for c in line)]
	empty_cols = [x for x, _ in enumerate(lines[0]) if all(line[x] == "." for line in lines)]

	galaxies = [(y, x) for y, line in enumerate(lines) for x, c in enumerate(line) if c == "#"]
	sum = 0
	for i , (x1, y1) in enumerate(galaxies):
		for (x2, y2) in galaxies[i+1:]:
			sum += abs(x2-x1) + abs(y2-y1)
			for p in empty_cols:
				if min(y1, y2) <= p <= max(y1, y2):
					sum += (factor - 1)
			for p in empty_lines:
				if min(x1, x2) <= p <= max(x1, x2):
					sum += (factor - 1)
	return sum

print(f"part 1 output = {space_walk(lines, 2)}")
print(f"part 2 output = {space_walk(lines, 1000000)}")
