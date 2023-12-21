from collections import deque

grid = open("input.txt").read().splitlines()

for y, line in enumerate(grid):
    for x, char in enumerate(line):
        if char == "S":
            start = (x, y)

## Part 1
q = deque([start])
for i in range(64):

    visited = deque()
    while len(q):

        x, y = q.popleft()
        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            ny = y + dy
            nx = x + dx

            if ny < 0 or ny >= len(grid) or nx < 0 or nx >= len(grid[0]) or grid[ny][nx] == "#" or (nx, ny) in visited:
                continue

            visited.append((nx, ny))

    q = visited

print(len(q))

## Part 2
# q = deque([start])
# for i in range(64):

#     visited = deque()
#     while len(q):

#         x, y = q.popleft()
#         for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
#             ny = y + dy
#             nx = x + dx

#             if grid[ny%len(grid)][nx%len(grid[0])] != "#" and (nx, ny) not in visited:
#                 visited.append((nx, ny))

#     q = visited

# print(len(q))
