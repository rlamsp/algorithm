import sys
sys.stdin = open('input.txt')









############################미완성 실패 코드#############################
# directions = {1: (-1, 0), 2: (1, 0), 3: (0, -1), 4: (0, 1)}
# opp = [2, 1, 4, 3]
# T = int(input())
# for tc in range(1, T+1):
#     N, M, K = map(int, input().split())
#     arr = [[-1]*N for _ in range(N)]
#     for n in range(N):  # 특수 약품이 있는 곳 = 0, 미생물이 움직일 수 있는 곳 = -1
#         arr[0][n] = 0
#         arr[n][0] = 0
#         arr[N-1][n] = 0
#         arr[n][N-1] = 0
#     for m in range(M):
#         for k in range(K):
#             i, j, A, D = map(int, input().split())
#             arr[i][j] = A
#             i, j = i + directions[D], j + directions[D]
#             if arr[i][j] == 0:
#                 A = A//2
#                 D = opp[D-1]
#                 arr[i][j] = A
#
#             else:
#                 arr[i][j] = A
#                 arr[i - directions[D]][j - directions[D]] = -1


