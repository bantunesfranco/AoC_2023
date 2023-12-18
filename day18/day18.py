lines = open("test.txt").read().strip().splitlines()

dirs = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}

def calc_area():
	area = abs(sum(dig[i][0] * (dig[i - 1][1] - dig[(i + 1)][1]) for i in range(1, len(dig) - 1))) // 2
	i = area - steps//2 + 1
	return i + steps

## Part 1
dig = [(0,0)]
steps = 0

for line in lines:

	dir, n, _ = line.split()

	n = int(n)
	steps += n

	x, y = dig[-1]
	dx, dy = dirs[dir]
	dig.append((x + dx * n, y + dy * n))

print(f"Part 1 output = {calc_area()}")


## Part 1
convert = ["R", "D", "L", "U"]
dig = [(0,0)]
steps = 0

for line in lines:

	_ , _ , color = line.split()
	color = color[2:-1]

	dir = convert[int(color[-1])]
	n = int(color[:-1], 16)
	
	steps += n

	x, y = dig[-1]
	dx, dy = dirs[dir]
	dig.append((x + dx * n, y + dy * n))
	
	
print(f"Part 2 output = {calc_area()}")