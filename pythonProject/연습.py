

di, dj  = (-1, 1, 0, 0), (0, 0, -1, 1)

def bfs():
    visited = [[0]*4 for _ in range(6)]
    q = []
    q.append((1, 0))

    while q:
        ci, cj = q.pop(0)

        for n in range(4):
            ni, nj = ci+di[n], cj+dj[n]

            if 0 <= ni < 4 and 0 <= nj < 6 and not visited[ni][nj]:
                q.append((ni, nj))


