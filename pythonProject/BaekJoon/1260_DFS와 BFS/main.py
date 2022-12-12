import sys
sys.stdin = open('input.txt')


def dfs(adj, V):
    global visited
    print(V, end=' ')
    visited[V] = 1

    if adj[V]:
        for W in adj[V]:
            if not visited[W]:
                dfs(adj, W)


def bfs(adj, V, N):
    visited = [0 for _ in range(N + 1)]
    queue = []
    queue.append(V)
    while queue:
        s = queue.pop(0)
        if not visited[s]:
            print(s, end=' ')
            visited[s] = 1
        if adj[s]:
            for i in adj[s]:
                if not visited[i]:
                    queue.append(i)


N, M, V = map(int, input().split())
adj = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

for _ in range(M):
    s, g = map(int, input().split())
    adj[s].append(g)
    adj[g].append(s)
for n in adj:
    n.sort()


dfs(adj, V)
print()
bfs(adj, V, N)






