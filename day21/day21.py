from collections import deque

grid = open("input.txt").read().splitlines()

for y, line in enumerate(grid):
	for x, char in enumerate(line):
		if char == "S":
			sx = x
			sy = y
			break

def count_steps(sx, sy, s):
	q = deque([(sx, sy, s)])
	visited = {(sx, sy)}
	res = set()

	while len(q):

		x, y, s = q.popleft()
		
		if s % 2 == 0:
			res.add((x, y))

		if s == 0:
			continue

		for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
			ny = y + dy
			nx = x + dx

			if not (0 <= ny < len(grid)) or not (0 <= nx < len(grid[0])) or grid[ny][nx] == "#" or (nx, ny) in visited:
				continue

			visited.add((nx, ny))
			q.append((nx, ny, s - 1))

	return len(res)

assert len(grid) == len(grid[0])
assert sx == sy == len(grid) // 2

## Part 1
print(f"Part 1 output = {count_steps(sx, sy, 64)}")

##part 2

steps = 26501365
size = len(grid)
grid_size = steps // size - 1

assert steps % size == size // 2

odd = (grid_size // 2 * 2 + 1) ** 2
even = ((grid_size + 1) // 2 * 2) ** 2


odd_points = count_steps(sx, sy, size * 2 + 1)
even_points = count_steps(sx, sy, size * 2)

corners = (count_steps(sx, 0, size - 1)
	+ count_steps(sx, size - 1, size - 1) 
	+ count_steps(size - 1, sy, size - 1)
    + count_steps(0, sy, size - 1))

small = (count_steps(0, size - 1, size // 2 - 1)
    + count_steps(size - 1, 0, size // 2 - 1) 
    + count_steps(0, 0, size // 2 - 1)
    + count_steps(size - 1, size - 1, size // 2 - 1))
 
big = (count_steps(0, size - 1, size * 3 // 2 - 1)
    + count_steps(size - 1, 0, size * 3 // 2 - 1) 
    + count_steps(0, 0, size * 3 // 2 - 1)
    + count_steps(size - 1, size - 1, size * 3 // 2 - 1))
 
res = odd * odd_points + even * even_points + corners + grid_size * big + (grid_size + 1) * small

print(f"Part 2 output = {res}")