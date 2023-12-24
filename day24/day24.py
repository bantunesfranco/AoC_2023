import sympy

data = open("input.txt").read().splitlines()
hailstones = [tuple(map(int, line.replace("@", ",").split(","))) for line in data]

## Part 1
def future_intersect(sx, sy, dx, dy, x, y):
    return ((x - sx) * dx >= 0 and (y - sy) * dy >= 0)

collisions = 0

# very fast, but complex
for i, h in enumerate(hailstones):
    for j, h2 in enumerate(hailstones[i+1:]):
        sx, sy, _, dx, dy, _ = h
        sx2, sy2, _, dx2, dy2, _ = h2

        a1, b1, c1 = dy, -dx, dy * sx - dx * sy
        a2, b2, c2 = dy2, -dx2, dy2 * sx2 - dx2 * sy2
        if a1 * b2 == a2 * b1:
            continue
        x = (b2 * c1 - b1 * c2) / (a1 * b2 - a2 * b1)
        y = (a1 * c2 - a2 * c1) / (a1 * b2 - a2 * b1)
        if  200000000000000 <= x <= 400000000000000 and 200000000000000 <= y <= 400000000000000\
        and all(future_intersect(sx, sy, dx, dy, x, y) for sx, sy, _, dx, dy, _ in [h, h2]):
            collisions += 1

# # very slow, but simple
# for i, h in enumerate(hailstones):
#     for j, h2 in enumerate(hailstones[:i]):
#         cx , cy = sympy.symbols("cx cy")
#         sol = sympy.solve([dy * (cx - sx) - dx * (cy - sy) for sx, sy, _, dx, dy, _ in (h, h2)])
#         if sol == []:
#             continue
#         x, y = sol[cx], sol[cy]
#         if  200000000000000 <= x <= 400000000000000 and 200000000000000 <= y <= 400000000000000\
#         and all(future_intersect(sx, sy, dx, dy, x, y) for sx, sy, _, dx, dy, _ in [h, h2]):
#             collisions += 1

print(f"Part 1 output = {collisions}")

## Part 2
cx, cy, cz, cdx, cdy, cdz = sympy.symbols("cx cy cz cdx cdy cdz")
equations = []

for i, (sx, sy, sz, dx, dy, dz) in enumerate(hailstones):
    equations.append((cx - sx) * (dy - cdy) - (cy - sy) * (dx - cdx))
    equations.append((cy - sy) * (dz - cdz) - (cz - sz) * (dy - cdy))

    if i < 2:
        continue
    solutions = [sol for sol in sympy.solve(equations)]
    if len(solutions) == 1:
        break

sol = solutions[0]

print(f"Part 2 output = {sol[cx] + sol[cy] + sol[cz]}")