with open("input.txt") as f:
    lines = f.read().splitlines()

plays = [(line.split()[0], int(line.split()[1])) for line in lines]

def best(hand):
    return (handType(hand), [letters.get(c, c) for c in hand])

## Part 1
letters = {"T":"A", "J":"B", "Q":"C", "K":"D", "A":"E"}

def handType(hand):
    cards = [hand.count(c) for c in hand]
    if 5 in cards:
        return 6
    if 4 in cards:
        return 5
    if 3 in cards and 2 in cards:
        return 4
    if 3 in cards:
        return 3
    if cards.count(2) == 4:
        return 2
    if 2 in cards:
        return 1
    return 0

plays.sort(key = lambda play: best(play[0]))

res = 0
for rank, (hand, bet) in enumerate(plays, 1):
    res += rank * bet

print(res)

## Part 2

letters = {"T":"A", "J":"1", "Q":"B", "K":"C", "A":"D"}

def handType(hand):
    cards = [hand.count(c) for c in hand if c != "J"]
    j = hand.count("J")

    if j == 5 or j == 4 or 5 in cards or (4 in cards and j == 1) or (3 in cards and j == 2) or (2 in cards and j == 3):
        return 6
    if 4 in cards or (3 in cards and j == 1) or (2 in cards and j == 2) or (1 in cards and j == 3):
        return 5
    if (3 in cards and 2 in cards) or (cards.count(2) == 4 and j == 1):
        return 4
    if 3 in cards or (2 in cards and j == 1) or (1 in cards and j == 2):
        return 3
    if cards.count(2) == 4:
        return 2
    if 2 in cards or (1 in cards and j == 1):
        return 1
    return 0

plays.sort(key = lambda play: best(play[0]))

res = 0
for rank, (hand, bet) in enumerate(plays, 1):
    res += rank * bet

print(res)