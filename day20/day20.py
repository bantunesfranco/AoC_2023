from collections import deque
import math

data = open("input.txt").read().splitlines()

class PulseModule:
	def __init__(self, data, key):
		self.id = key
		self.type = data[0][0]
		self.target = data[1].split(", ")
		self.state = False
		self.history = {} if self.type == "&" else ""
	
	def __repr__(self) -> str:
		return f"{self.id}: type= {self.type}, targets= {', '.join(self.target)}" + (f", hist= {self.history}" if self.type == "&" else "")

data = [line.split(" -> ") for line in data]

Modules = {}
for line in data:
	key = line[0][1:] if line[0] != "broadcaster" else "broadcaster"
	Modules[key] = PulseModule(line, key)

for key, module in Modules.items():
	for t in module.target:
		if t in Modules and Modules[t].type == "&":
			Modules[t].history[key] = 0

## Part 1
lowPulse = 0
highPulse = 0
for _ in range(1000):

	lowPulse += 1
	q = deque([("broadcaster", t, 0) for t in  Modules["broadcaster"].target])

	while len(q):
		sender, target, pulse = q.popleft()
		
		if pulse == 1:
			highPulse += 1
		else:
			lowPulse += 1

		m = Modules.get(target, None)
		if m == None:
			continue

		if m.type == "%":
			if pulse == 0:
				m.state = True if m.state == False else False
				for t in m.target:
					q.append((m.id, t, m.state))
		elif m.type == "&":
			m.history[sender] = pulse
			p = 0 if all(pulse == 1 for pulse in m.history.values()) else 1
			for t in m.target:
				q.append((m.id, t, p))

print(f"Part 1 output = {lowPulse * highPulse}")

## Part 2
for key, module in Modules.items():
	module.state = False
	for t in module.target:
		if t in Modules and Modules[t].type == "&":
			Modules[t].history[key] = 0

last = [id for id, module in Modules.items() if "rx" in module.target]
assert len(last) == 1
last = last[0]

cycles = {}
seen = {id : 0 for id, module in Modules.items() if last in module.target}

buttonPress  = 0

while True:
	buttonPress += 1
	q = deque([("broadcaster", t, 0) for t in  Modules["broadcaster"].target])

	while len(q):
		sender, target, pulse = q.popleft()

		if target not in Modules:
			continue

		m = Modules[target]
		
		if m.id == last and pulse == 1:
			seen[sender] += 1

			if sender not in cycles:
				cycles[sender] = buttonPress
			else:
				assert buttonPress ==  seen[sender] * cycles[sender]

			if all(seen.values()):
				lcm = 1
				for cycle in cycles.values():
					lcm = lcm * cycle // math.gcd(lcm, cycle)
				print(f"Part 2 output = {lcm}")
				exit(0)

		if m.type == "%":
			if pulse == 0:
				m.state = True if m.state == False else False
				for t in m.target:
					q.append((m.id, t, m.state))
		elif m.type == "&":
			m.history[sender] = pulse
			p = 0 if all(pulse == 1 for pulse in m.history.values()) else 1
			for t in m.target:
				q.append((m.id, t, p))
