with open("./input.txt", 'r') as f:
	lines = f.readlines()

## PART 1
output = 0
for line in lines:
	in_line = [c for c in line if c.isdigit()]
	output += int(in_line[0] + in_line[-1])

print(f"Part 1 output = {output}")

## PART 2
output = 0
for line in lines:
	in_line = []
	for i , c in enumerate(line):
		if c.isdigit():
			in_line.append(c)
		else:
			for j, w in enumerate(["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
				if line[i:].startswith(w):
					in_line.append(str(j+1))
					break
	output += int(in_line[0] + in_line[-1])

print(f"Part 2 output = {output}")