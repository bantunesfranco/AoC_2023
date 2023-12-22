from collections import deque

bricks = [list(map(int, line.replace("~", ",").strip().split(","))) for line in open("input.txt")]
bricks.sort(key=lambda brick: brick[2])

def is_overlapping(a, b):
    return max(a[0], b[0]) <= min(a[3], b[3]) and max(a[1], b[1]) <= min(a[4], b[4])

for i, brick in enumerate(bricks):
    min_z = 1
    for j, brick2 in enumerate(bricks[:i]):
        if is_overlapping(brick, brick2):
            min_z = max(min_z, brick2[5] + 1)

    brick[5] -= brick[2] - min_z
    brick[2] = min_z

supports = {i : set() for i in range(len(bricks))}
supported = {i : set() for i in range(len(bricks))}

for i, top_brick in enumerate(bricks):
    for j, bot_brick in enumerate(bricks[:i]):
        if is_overlapping(top_brick, bot_brick) and top_brick[2] == bot_brick[5] + 1:
            supports[j].add(i)
            supported[i].add(j)

## Part 1
res = 0
for i in range(len(bricks)):
    if all(len(supported[j]) >= 2 for j in supports[i]):
        res += 1

print(f"Part 1 output = {res}")

## Part 2

res = 0
for i in range(len(bricks)):
    
    q = deque([j for j in supports[i] if len(supported[j]) == 1])
    fall = set(q)
    fall.add(i)
    
    while len(q):
        
        j = q.popleft()
        for k in supports[j]:
            if k not in fall and all(l in fall for l in supported[k]):
                q.append(k)
                fall.add(k)

    res += len(fall) - 1
    
print(f"Part 2 output = {res}")