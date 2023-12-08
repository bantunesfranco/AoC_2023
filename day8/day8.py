import math

with open("input.txt") as f:
    move, *data = f.read().splitlines()

paths={}
for line in data:
    if line == "":
        continue
    key, value = line.split(" = ")
    paths[key] = value.strip("()").split(", ")

# Part 1
start = "AAA"
steps = 0
i = 0
while start != "ZZZ":
    if move[i] == "L":
        start = paths[start][0]
    elif move[i] == "R":
        start = paths[start][1]
    steps += 1
    i = 0 if i + 1 == len(move) else i+1
print(f"Part 1 output = {steps}")

# Part 2
start = [path for path in paths if path.endswith("A")]
loops = []
for s in start:
    steps = 0
    i = 0
    z1 = None
    loop = []
    while True:
        while steps == 0 or not s.endswith("Z"):
            if move[i] == "L":
                s = paths[s][0]
            elif move[i] == "R":
                s = paths[s][1]
            steps += 1
            i = 0 if i + 1 == len(move) else i+1

        loop.append(steps)

        if z1 is None:
            z1 = s
            steps = 0
        elif s == z1:
            break
    loops.append(loop)

zlist = [loop[0] for loop in loops]

lcm = zlist[0]
for z in zlist[1:]:
    lcm = lcm * z // math.gcd(lcm, z)

print(f"Part 2 output = {lcm}")

