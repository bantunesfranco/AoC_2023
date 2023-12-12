import functools

with open("input.txt") as f:
	lines = f.read().strip().splitlines()

@functools.lru_cache(maxsize=None)
def match(springs, damage) -> int:
	if springs == "":
		if len(damage) == 0:
			return 1
		return 0
	
	if len(damage) == 0:
		if "#" in springs:
			return 0
		return 1
	
	res = 0
	if springs[0] in ".?":
		res += match(springs[1:], damage)
	
	if springs[0] in "#?":
		if damage[0] <= len(springs) and "." not in springs[:damage[0]] \
		and (damage[0] == len(springs) or springs[damage[0]] != "#"):
			res += match(springs[damage[0]+1:], damage[1:])

	return res

## Part 1
res = 0
for line in lines:
	springs , damage = line.split()
	damage = tuple(map(int, damage.split(",")))
	res += match(springs, damage)

print(res)

## Part 2
res = 0
for line in lines:
	springs , damage = line.split()
	springs += ("?"+springs)*4
	damage = tuple(map(int, damage.split(",")*5))
	res += match(springs, damage)

print(res)
