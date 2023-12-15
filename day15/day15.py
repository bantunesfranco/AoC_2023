input = open("input.txt").read().strip().split(",")

## Part 1

res = []
for i in input:
    v = 0
    for j in i:
        v = (v + ord(j)) * 17 % 256
    res.append(v)

print(f"Part 1 output = {sum(res)}")

## Part 2

boxes = [{} for _ in range(256)]
for item in input:
    v = 0
    for j in item:
        if j == "=" or j == "-":
            break
        v = (v + ord(j)) * 17 % 256
    if "=" in item:
        hash, lens = item.split("=")
        boxes[v][hash] = int(lens)
    else:
        hash = item[:-1]
        for box in boxes:
            if hash in box:
                box.pop(hash)
                break

res = []
for i, box in enumerate(boxes, 1):
    for hash in box:
        v = i * (list(box).index(hash) + 1) * box[hash]
        res.append(v)

print(f"Part 2 output = {sum(res)}")