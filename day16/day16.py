from collections import deque

grid = open("input.txt").read().strip().splitlines()

def find_path(y, x, dy, dx):
    start = [(y, x, dy, dx)]
    visited = set()
    q = deque(start)

    while len(q):
        y, x , dy, dx = q.popleft()
        
        y += dy
        x += dx
        if not 0 <= y < len(grid) or not 0 <= x < len(grid[y]):
            continue
        
        c = grid[y][x]
        if c == "|" and dx != 0:
            for dy, dx, in [(1, 0), (-1, 0)]:
                if (y, x, dy, dx) not in visited:
                    q.append((y, x, dy, dx))
                    visited.add((y, x, dy, dx))
        elif c == "-" and dy != 0:
            for dy, dx, in [(0, 1), (0, -1)]:
                if (y, x, dy, dx) not in visited:
                    q.append((y, x, dy, dx))
                    visited.add((y, x, dy, dx))
        elif c == "/":
            dy, dx = -dx, -dy
            if (y, x, dy, dx) not in visited:
                q.append((y, x, dy, dx))
                visited.add((y, x, dy, dx))
        elif c == "\\":
            dy, dx = dx, dy
            if (y, x, dy, dx) not in visited:
                q.append((y, x, dy, dx))
                visited.add((y, x, dy, dx))
        else:
            if (y, x, dy, dx) not in visited:
                q.append((y, x, dy, dx))
                visited.add((y, x, dy, dx))

    return len(set((x, y) for y, x, _, _ in visited))

# Part 1
res = find_path(0, -1, 0, 1)
print(f"Part 1 output = {res}")

# Part 2

runs = []
for y in range(len(grid)):
    runs.append(find_path(y, -1, 0, 1))
    runs.append(find_path(y, len(grid[y]), 0, -1))

for x in range(len(grid[0])):
    runs.append(find_path(-1, x, 1, 0))
    runs.append(find_path(len(grid), x, -1, 0))

print(f"Part 2 output = {max(runs)}")
