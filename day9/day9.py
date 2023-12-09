with open("input.txt") as f:
	data = f.read().splitlines()

# Part 1
res = []
for line in data:
	line = list(map(int, line.split()))
	history = [line]
	while True:
		his = []
		for i, _ in enumerate(line):
			if i == len(line) - 1:
				break
			his.append(line[i + 1] - line[i])

		history.append(his)
		line = his
		if his == [0] * len(his):
			break

	for i, item in reversed(list(enumerate(history))):
		if i == len(history) - 1:
			item.append(0)
		else:
			item.append(history[i + 1][-1] + item[-1])
	res.append(history[0][-1])

print(f"Part 1 output = {sum(res)}")

## Part 2
res = []
for line in data:
	line = list(map(int, line.split()))
	history = [line]
	while True:
		his = []
		for i, _ in enumerate(line):
			if i == len(line) - 1:
				break
			his.append(line[i + 1] - line[i])

		history.append(his)
		line = his
		if his == [0] * len(his):
			break

	for i, item in reversed(list(enumerate(history))):
		if i == len(history) - 1:
			history[i] = [0] + item
		else:
			history[i] = [item[0] - history[i + 1][0]] + item

	res.append(history[0][0])

print(f"Part 2 output = {sum(res)}")


## recursive solution

def calc_diff(array, part):
	if all(n == 0 for n in array):
		return 0

	diffs = [n2 - n1 for n1, n2 in zip(array, array[1:])]
	diff = calc_diff(diffs, part)
	if part == 1:
		return array[-1] + diff
	else:
		return array[0] - diff

res = 0
for line in data:
	line = list(map(int, line.split()))
	res += calc_diff(line, 1)
 
print(f"Part 1 output = {res}")

res = 0
for line in data:
	line = list(map(int, line.split()))
	res += calc_diff(line, 2)
 
print(f"Part 2 output = {res}")