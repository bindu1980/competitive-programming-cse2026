class Edge:
    def __init__(self, to, cap, rev):
        self.to = to
        self.cap = cap
        self.rev = rev


def add_edge(u, v, cap):
    graph[u].append(Edge(v, cap, len(graph[v])))
    graph[v].append(Edge(u, 0, len(graph[u]) - 1))


def dfs(u, t, f):
    if u == t:
        return f

    visited[u] = True

    for e in graph[u]:
        if e.cap > 0 and not visited[e.to]:
            d = dfs(e.to, t, min(f, e.cap))

            if d > 0:
                e.cap -= d
                graph[e.to][e.rev].cap += d
                return d

    return 0


V, E = map(int, input().split())

graph = [[] for _ in range(V)]

for _ in range(E):
    u, v, c = map(int, input().split())
    add_edge(u, v, c)

source = 0
sink = V - 1
answer = 0

while True:
    visited = [False] * V
    f = dfs(source, sink, 10**18)

    if f == 0:
        break

    answer += f

print(answer)
