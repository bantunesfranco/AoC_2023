
## Part 1 first attempt
# workflows, parts = open('input.txt').read().strip().split("\n\n")

# workflows = {wf.strip("}").split("{")[0]:tuple(wf.strip("}").split("{")[1].split(",")) for wf in workflows.splitlines()}
# parts = [part.strip("{}").split(",") for part in parts.splitlines()]
# parts = [{p.split("=")[0]:int(p.split("=")[1]) for p in part} for part in parts ]

# accepted = []
# for part in parts:
#     x = part["x"]
#     m = part["m"]
#     a = part["a"]
#     s = part["s"]
#     w = workflows["in"]
#     i = 0
#     while True:
#         b = False
#         if ":" in w[i]:
#             cond, eff = w[i].split(":")
#             if eval(cond) == True:
#                 if eff == "R":
#                     b = True
#                     break
#                 elif eff == "A":
#                     b = True
#                     accepted.append(part)
#                     break
#                 else:
#                     w = workflows[eff]
#                     i = 0
#                     continue
#             else:
#                 i += 1
#                 continue
#         elif w[i] == "R":
#             b = True
#             break
#         elif w[i] == "A":
#             b = True
#             accepted.append(part)
#             break
#         else:
#             w = workflows[w[i]]
#             i = 0
#         if b == True:
#             break

# print(f"Part 1 output = {sum(list(sum(int(part[i]) for i in part) for part in accepted))}")

### second attempt
b1, b2 = open('input.txt').read().strip().split("\n\n")

workflows = {}

for line in b1.splitlines():
    name, value = line.strip("}").split("{")
    rules = value.split(",")
    workflows[name] = ([], rules.pop())
    for rule in rules:
        comparison, target = rule.split(":")
        key = comparison[0] 
        c = comparison[1]
        n = int(comparison[2:])
        workflows[name][0].append((key, c, n, target))

## Part 1 
def accept(part, name = "in"):
    if name == "A":
        return True

    if name == "R":
        return False

    rules = workflows[name][0]
    for rule in rules:
        key, c, n, target = rule

        if c == ">":
            if part[key] > n:
                return accept(part, target)

        elif c == "<":
            if part[key] < n:
                return accept(part, target)

    return accept(part, workflows[name][1])

res = 0
for line in b2.splitlines():
    part = {}
    for pair in line.strip("{}").split(","):
        key, value = pair.split("=")
        part[key] = int(value)

    if accept(part):
        res += sum(part.values())

print(f"Part 1 output = {res}")

## Part 2

def check_range(ranges ,name = "in"):

    if name == "A":
        p = 1
        for start, end in ranges.values():
            p = p * (end - start + 1)
        return p

    if name == "R":
        return 0
    
    res = 0
    rules = workflows[name][0]

    for rule in rules:
        key, c, n, target = rule
        start, end = ranges[key]
        
        if c == "<":
            yes = (start, n - 1)
            no = (n, end)
        else:
            yes = (n + 1, end)
            no = (start, n)

        if yes[0] <= yes[1]:
            newRanges = dict(ranges)
            newRanges[key] = yes
            res += check_range(newRanges, target)

        if no[0] <= no[1]:
            ranges = dict(ranges)
            ranges[key] = no
        else:
            break

    else:
        res += check_range(ranges, workflows[name][1])

    return res

print(f"Part 2 output = {check_range({key : (1, 4000) for key in 'xmas'})}")
