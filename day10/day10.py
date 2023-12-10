from collections import deque

with open("input.txt") as f:
	data = f.read().splitlines()

start = ()
for y, line in enumerate(data):
	for x, char in enumerate(line):
		if char == "S":
			start = (x, y)
			break
	if len(start) != 0:
		break

## part 1
visited = {start}
q = deque([start])

while len(q):
	x, y = q.popleft()
	c = data[y][x]

	if (not (0 <= y < len(data)) or not (0 <= x < len(data[0]))):
		continue
	
	if c in "S|JL" and data[y - 1][x] in "|7F" and (x, y - 1) not in visited:
		q.append((x, y - 1))
		visited.add((x, y - 1))
	if c in "S|7F" and data[y + 1][x] in "|JL" and (x, y + 1) not in visited:
		q.append((x, y + 1))
		visited.add((x, y + 1))
	if c in "S-J7" and data[y][x - 1] in "-LF" and (x - 1, y) not in visited:
		q.append((x - 1, y))
		visited.add((x - 1, y))
	if c in "S-LF" and data[y][x + 1] in "-J7" and (x + 1, y) not in visited:
		q.append((x + 1, y))
		visited.add((x + 1, y))

print(f"output part 1 = {len(visited)//2}")

## part 2
visited = {start}
q = deque([start])
start_value = ["|", "-", "7", "F", "J", "L"]

while len(q):
	x, y = q.popleft()
	c = data[y][x]

	if (not (0 <= y < len(data)) or not (0 <= x < len(data[0]))):
		continue
	
	if c in "S|JL" and data[y - 1][x] in "|7F" and (x, y - 1) not in visited:
		q.append((x, y - 1))
		visited.add((x, y - 1))
		if c == "S":
			start_value = [c for c in start_value if c in "|JL"]
	if c in "S|7F" and data[y + 1][x] in "|JL" and (x, y + 1) not in visited:
		q.append((x, y + 1))
		visited.add((x, y + 1))
		if c == "S":
			start_value = [c for c in start_value if c in "|7F"]
	if c in "S-J7" and data[y][x - 1] in "-LF" and (x - 1, y) not in visited:
		q.append((x - 1, y))
		visited.add((x - 1, y))
		if c == "S":
			start_value = [c for c in start_value if c in "-J7"]
	if c in "S-LF" and data[y][x + 1] in "-J7" and (x + 1, y) not in visited:
		q.append((x + 1, y))
		visited.add((x + 1, y))
		if c == "S":
			start_value = [c for c in start_value if c in "-LF"]

assert len(start_value) == 1
start_value = start_value[0]

data = [y.replace("S", start_value) for y in data]
data = ["".join(c if (x, y) in visited else "." for x, c in enumerate(r)) for y, r in enumerate(data)]

outside = set()

for y, row in enumerate(data):
	vert = None
	in_pipe = False
	for x, c in enumerate(row):
		if c == "|":
			in_pipe = not in_pipe
		elif c in "LF":
			if c == "L":
				vert = True
			else:
				vert = False
		elif c in "J7":
			if (vert and c != "J") or (not vert and c != "7"):
				in_pipe = not in_pipe
			vert = None
		elif c in "-.":
			pass
		if not in_pipe:
			outside.add((x, y))

print(f"output part 2 = {len(data)*len(data[0]) - len(visited | outside)}")