from heapq import heappush, heappop

grid = [list(map(int, line.strip())) for line in open("input.txt")]

## Part 1
hq = [(0,0,0,0,0,0)]
visited = set()

while len(hq):
	
	h, d, y, x, dy, dx = heappop(hq)

	if y == len(grid) - 1 and x == len(grid[0]) - 1:
		print(f"Part 1 output = {h}")
		break
	
	if (d, y, x, dy, dx) in visited:
		continue
	
	visited.add((d, y, x, dy, dx))
	
	if d < 3 and (dy, dx) != (0,0):
		ny = y + dy
		nx = x + dx
		if 0 <= ny < len(grid) and 0 <= nx < len(grid[0]):
			heappush(hq, (h+grid[ny][nx], d+1, ny, nx, dy, dx))
	
	for ndy, ndx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
		if (ndy, ndx) != (dy, dx) and (ndy, ndx) != (-dy, -dx):
			ny = y + ndy
			nx = x + ndx
			if 0 <= ny < len(grid) and 0 <= nx < len(grid[0]):
				heappush(hq, (h+grid[ny][nx], 1, ny, nx, ndy, ndx))

## Part 2
hq = [(0,0,0,0,0,0)]
visited = set()

while len(hq):
	
	h, d, y, x, dy, dx = heappop(hq)

	if y == len(grid) - 1 and x == len(grid[0]) - 1:
		print(f"Part 1 output = {h}")
		break
	
	if (d, y, x, dy, dx) in visited:
		continue
	
	visited.add((d, y, x, dy, dx))
	
	if d < 10 and (dy, dx) != (0,0):
		ny = y + dy
		nx = x + dx
		if 0 <= ny < len(grid) and 0 <= nx < len(grid[0]):
			heappush(hq, (h+grid[ny][nx], d+1, ny, nx, dy, dx))

	if d >= 4 or (dy, dx) == (0,0):
		for ndy, ndx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
			if (ndy, ndx) != (dy, dx) and (ndy, ndx) != (-dy, -dx):
				ny = y + ndy
				nx = x + ndx
				if 0 <= ny < len(grid) and 0 <= nx < len(grid[0]):
					heappush(hq, (h+grid[ny][nx], 1, ny, nx, ndy, ndx))
