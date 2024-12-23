import sys
from collections import defaultdict


def bron_kerbosch(R, P, X, graph):
    if not P and not X:
        yield R
    while P:
        v = P.pop()
        yield from bron_kerbosch(R.union({v}), P.intersection(graph[v]), X.intersection(graph[v]), graph)
        X.add(v)


edges = [tuple(i.split("-")) for i in sys.stdin.read().split("\n")]
graph = defaultdict(set)
for u, v in edges:
    graph[u].add(v)
    graph[v].add(u)
graph = {key: set(graph[key]) for key in graph}
print(*sorted(max(bron_kerbosch(set(), set(graph.keys()), set(), graph), key=len)), sep=",")
