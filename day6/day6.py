with open("input.txt") as f:
    lines = f.read().splitlines()

## Part 1
time = list(map(int, lines[0].split(":")[1].split()))
dist = list(map(int, lines[1].split(":")[1].split()))

res = [0] * len(time)
for i in range(len(time)):
    for t in range(time[i] + 1):
        d = (time[i] - t) * t
        if (d > dist[i]):
            res[i] += 1

output = 1
for i in res:
    output *= i

print(f"Part 1 output = {output}")

## Part 2
time = int("".join(lines[0].split(":")[1].split()))
dist = int("".join(lines[1].split(":")[1].split()))

res = 0
for t in range(time + 1):
    d = (time - t) * t
    if (d > dist):
        res += 1

print(f"Part 2 output = {res}")