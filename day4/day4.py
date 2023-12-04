import re

with open("input.txt") as f:
	lines = f.read().splitlines()

## Part 1

points = 0
for line in lines:
	lists = line.split(":")[1].split("|")
	winners = set(re.findall("\d+", lists[0]))
	mine = set(re.findall("\d+", lists[1]))

	found = sum(number in mine for number in winners) - 1

	if found != -1:
		points += 2**found

print(f"Part 1 output = {points}")

## Part 2

cards = {}
for i, line in enumerate(lines):
	if i not in cards:
		cards[i] = 1

	lists = line.split(":")[1].split("|")
	winners = set(re.findall("\d+", lists[0]))
	mine = set(re.findall("\d+", lists[1]))

	found = sum(number in winners for number in mine)

	for j in range(i + 1, i + found + 1):
		cards[j] = cards.get(j, 1) + cards[i]

print(f"Part 2 output = {sum(cards.values())}")