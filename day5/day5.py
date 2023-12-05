with open("input.txt") as f:
	first, *blocks = f.read().split("\n\n")

## Part 1
seeds = list(map(int, first.split(":")[1].split()))

for block in blocks:
	ranges = []
	for line in block.splitlines()[1:]:
		ranges.append(list(map(int, line.split())))

	res = []
	for seed in seeds:
		for a, b, c in ranges:
			if seed in range(b, b + c):
				res.append(seed - b + a)
				break
		else:
			res.append(seed)
	seeds = res

print(f"Part 1 output = {min(seeds)}")

## Part 2

inputs = list(map(int, first.split(":")[1].split()))

seeds = []
i = 0
for i in range(0, len(inputs), 2):
	seeds.append((inputs[i], inputs[i] + inputs[i + 1]))

for block in blocks:
	ranges = []
	for line in block.splitlines()[1:]:
		ranges.append(list(map(int, line.split())))

	res = []
	while len(seeds) > 0:
		s, e = seeds.pop()
		for a, b, c in ranges:
			os = max(s, b)
			oe = min(e, b + c)
			if os < oe:
				res.append((os - b + a, oe - b + c))
				if os > s:
					seeds.append((s, os))
				if e > oe:
					seeds.append((oe, e))
				break
		else:
			res.append((s, e))
		seeds = res

print(f"Part 2 output = {seeds[0]}")