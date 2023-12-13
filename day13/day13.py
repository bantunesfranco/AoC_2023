with open("input.txt") as f:
    blocks = f.read().split("\n\n")

## part 1
def find_mirror(block) -> int:
    for i in range(1, len(block)):
        m1 = block[:i][::-1]
        m2 = block[i:]
        
        l1 = len(m1)
        l2 = len(m2)
        if l1 < l2:
            m2 = m2[:l1]
        elif l2 < l1:
            m1 = m1[:l2]
        
        if m1 == m2:
            return i
    return 0

res = 0
for block in blocks:
    block = block.split()
    res += (find_mirror(block)*100)
    res += find_mirror(list(zip(*block)))

print(f"Part 1 output = {res}")

## part 2
def find_mirror(block) -> int:
    for i in range(1, len(block)):
        m1 = block[:i][::-1]
        m2 = block[i:]

        smudge = 0
        for x, y in zip(m1, m2):
            for a, b in zip(x, y):
                if a != b:
                    smudge += 1

        if smudge == 1:
            return i
    return 0

res = 0
for block in blocks:
    block = block.split()
    res += (find_mirror(block)*100)
    res += find_mirror(list(zip(*block)))

print(f"Part 2 output = {res}")