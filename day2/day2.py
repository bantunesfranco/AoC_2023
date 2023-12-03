with open("input.txt") as f:
	lines = f.readlines()
	
## Part 1
games = 0 

for i, line in enumerate(lines, start=1):
	line = line.split(":")[1].strip().split(";")
	cubes = {"red":0, "green":0, "blue":0}
	for set in line:
		pulls = set.split(",")
		for item in pulls:
			item = item.strip(" ")
			value, key = item.split(" ")
			if int(value) > cubes[key]:
				cubes[key] = int(value)
	if cubes["red"] <= 12 and cubes["green"] <= 13 and cubes["blue"] <= 14:
		games += i

print(f"Part 1 output = {games}")

## Part 2

total_power = 0 

for i, line in enumerate(lines, start=1):
	line = line.split(":")[1].strip().split(";")
	cubes = {"red":0, "green":0, "blue":0}
	for set in line:
		pulls = set.split(",")
		for item in pulls:
			item = item.strip(" ")
			value, key = item.split(" ")
			if int(value) > cubes[key]:
				cubes[key] = int(value)
	total_power += (cubes["red"] * cubes["green"] * cubes["blue"])

print(f"Part 1 output = {total_power}")