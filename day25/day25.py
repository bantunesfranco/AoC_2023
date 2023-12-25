from igraph import Graph

graph = {key : value.split() for key, value in [line.split(": ") for line in open("input.txt")]}
a, b = Graph.ListDict(graph).mincut().sizes()

print(f"Part 1 output = {a * b}")