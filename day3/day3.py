import re

with open("input.txt") as f:
	grid = f.read().splitlines()

## Part 1
coords = set()
for y, line in enumerate(grid):
	for x, char in enumerate(line):
		if char == '.' or char.isdigit():
			continue
		for ny in range(y-1, y+2):
			for nx in range(x-1, x+2):
				if ny < 0 or ny >= len(grid) or nx < 0 or  nx >= len(grid[ny]) or not grid[ny][nx].isdigit():
					continue
				while nx > 0 and grid[ny][nx-1].isdigit():
					nx -= 1
				coords.add((ny, nx))

numbers = []
for y, x in coords:
	s = ""
	while x < len(grid[y]) and grid[y][x].isdigit():
		s += grid[y][x]
		x += 1
	numbers.append(int(s))

print(f"Part 1 output = {sum(numbers)}")

## Part 2
numbers = []
for y, line in enumerate(grid):
	for x, char in enumerate(line):
		if char != "*":
			continue
		coords = set()
		for ny in range(y-1, y+2):
			for nx in range(x-1, x+2):
				if ny < 0 or ny >= len(grid) or nx < 0 or  nx >= len(grid[ny]) or not grid[ny][nx].isdigit():
					continue
				while nx > 0 and grid[ny][nx-1].isdigit():
					nx -= 1
				coords.add((ny, nx))

		if len(coords) != 2:
			continue
		ratio = 1
		for ny, nx in coords:
			s = ""
			while nx < len(grid[ny]) and grid[ny][nx].isdigit():
				s += grid[ny][nx]
				nx += 1
			ratio *= int(s)
		numbers.append(ratio)

print(f"Part 1 output = {sum(numbers)}")