from collections import deque

grid = open('input.txt').read().splitlines()

#### Attempt 1
# start = (1, 0, 0, 1, 0)
# end = (len(grid[0]) - 2, len(grid) - 1)

# steps = []
# newpath = [(start, set())]

# for pos, visited in newpath:

# 	q = deque([pos])

# 	while len(q):
# 		x, y, dx, dy, s = q.popleft()

# 		if (x, y) in visited:
# 			continue

# 		if not (0 <= x < len(grid)) or not (0 <= y < len(grid[0])):
# 			continue
		
# 		visited.add((x, y))
# 		if (x, y) == end:
# 			steps.append(s)
# 			break

# 		paths = 0
# 		for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
# 			nx = x + dx
# 			ny = y + dy
# 			if not (0 <= nx < len(grid)) or not (0 <= ny < len(grid[0])):
# 				continue
# 			if grid[ny][nx] == "^" and dy != -1 or grid[ny][nx] == "v" and dy != 1 or grid[ny][nx] == "<" and dx != -1 or grid[ny][nx] == ">" and dx != 1:
# 				continue
# 			if grid[ny][nx] != '#' and (nx, ny) not in visited:
# 				if paths == 0:
# 					q.append((nx, ny, dx, dy, s + 1))
# 					paths += 1
# 				else:
# 					newpath.append(((nx, ny, dx, dy, s + 1), set(visited)))

# print(max(steps))

#### Attempt 2
def inBounds(x, y):
	return (0 <= y < len(grid) and 0 <= x < len(grid[0]) and grid[y][x] != "#")

def dfs(p):
	if p == end:
		return 0
	
	visited.add(p)

	d = -float('inf')
	for np in graph[p]:
		if np not in visited:
			d = max(d, dfs(np) + graph[p][np])

	visited.remove(p)

	return d

start = (1, 0)
end = (len(grid[0]) - 2, len(grid) - 1)

points = [start, end]
for y, line in enumerate(grid):
	for x, c in enumerate(line):

		if c == "#":
			continue

		paths = 0
		for nx, ny in [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]:
			if inBounds(nx, ny):
				paths += 1

		if paths > 2:
			points.append((x, y))

dirs = {
	"^": [(0, -1)],
	"v": [(0, 1)],
	"<": [(-1, 0)],
	">": [(1, 0)],
	".": [(0, -1), (0, 1), (-1, 0), (1, 0)]
}

## Part 1
graph = {p : {} for p in points}
for sx, sy in points:
	q = deque([(sx, sy, 0)])
	visited = {(sx, sy)}

	while len(q):
		x, y, d = q.popleft()

		if d != 0 and (x, y) in points:
			graph[(sx, sy)][(x, y)] = d
			continue

		for dx, dy in dirs[grid[y][x]]: 
			nx = x + dx
			ny = y + dy
			if inBounds(nx, ny) and (nx, ny) not in visited:
				q.append((nx, ny, d + 1))
				visited.add((nx, ny))

visited = set()

print(f"Part 1 output = {dfs(start)}")

## Part 2
graph = {p : {} for p in points}
for sx, sy in points:
	q = deque([(sx, sy, 0)])
	visited = {(sx, sy)}

	while len(q):
		x, y, d = q.popleft()

		if d != 0 and (x, y) in points:
			graph[(sx, sy)][(x, y)] = d
			continue

		for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]: 
			nx = x + dx
			ny = y + dy
			if inBounds(nx, ny) and (nx, ny) not in visited:
				q.append((nx, ny, d + 1))
				visited.add((nx, ny))

visited = set()

print(f"Part 2 output = {dfs(start)}")