with open("input.txt") as f:
	lines = f.read().splitlines()

points = 0
cards = {}

for i, line in enumerate(lines):
	if i not in cards:
		cards[i] = 1
	lists = line.split(":")[1].split("|")
	winners = lists[0].split()
	mine = lists[1].split()

	## Part 1
	found = sum(n in mine for n in winners) - 1
	if found != -1:
		points += 2**found

	## Part 2
	found = sum(n in mine for n in winners)
	for j in range(i + 1, i + found + 1):
		cards[j] = cards.get(j, 1) + cards[i]

print(f"Part 1 output = {points}")
print(f"Part 2 output = {sum(cards.values())}")
