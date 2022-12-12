import sys
import heapq
from collections import deque
input = sys.stdin.readline


# def dijkstra(start):
#     dp[start] = 0
#     heapq.heappush(heap, (0, start))
#
#     while heap:
#         now_dist, now_node = heapq.heappop(heap)
#
#         if dp[now_node] < now_dist:
#             continue
#
#         for next_node in graph[now_node]:
#             next_dist = now_dist + 1
#             if next_dist < dp[next_node]:
#                 dp[next_node] = next_dist
#                 heapq.heappush(heap, (next_dist, next_node))
#
#
# N, M = map(int, input().split())
# graph = [[] for _ in range(N+1)]
# for n in range(M):
#     A, B = map(int, input().split())
#     graph[A].append(B)
#     graph[B].append(A)
#
# heap = []
# INF = sys.maxsize
# dp = [INF]*(N+1)
# dijkstra(1)
# max_dist = 0
# for dist in dp:
#     if dist != INF and max_dist < dist:
#         max_dist = dist
#
# cnt = 0
# for i in dp:
#     if i == max_dist:
#         cnt += 1
#
# max_node = dp.index(max_dist)
#
# print(max_node, max_dist, cnt, end=' ')


def bfs(start):
    queue = deque()
    queue.append((start, 0))
    visited[start] = 0

    while queue:
        now_node, dist = queue.popleft()
        for next_node in graph[now_node]:
            if visited[next_node] == -1:
                queue.append((next_node, dist + 1))
                visited[next_node] = dist + 1


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for n in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

visited = [-1]*(N+1)
bfs(1)
max_dist = max(visited)
max_node = visited.index(max_dist)
cnt = 0
for i in visited:
    if i == max_dist:
        cnt += 1

print(max_node, max_dist, cnt, end=' ')


# def bfs(start):
#     queue = deque()
#     queue.append(start)
#     visited[start] = 1
#
#     while queue:
#         now_node = queue.popleft()
#         for next_node in graph[now_node]:
#             if not visited[next_node]:
#                 queue.append(next_node)
#                 visited[next_node] = visited[now_node] + 1
#
#
# N, M = map(int, input().split())
# graph = [[] for _ in range(N+1)]
# for n in range(M):
#     A, B = map(int, input().split())
#     graph[A].append(B)
#     graph[B].append(A)
#
# visited = [0]*(N+1)
# bfs(1)
# max_dist = max(visited)
# max_node = visited.index(max_dist)
# cnt = visited.count(max_dist)
#
# print(max_node, max_dist-1, cnt, end=' ')
