import sys
sys.stdin = open('input.txt')

###################################알고리즘 교수님 풀이#####################################
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0]*(N+1) for _ in range(N+1)]
    arr[N//2][N//2] = arr[N//2+1][N//2+1] = 2  # 초기 돌 놓기
    arr[N//2+1][N//2] = arr[N//2][N//2+1] = 1  # 초기 돌 놓기

    for _ in range(M):
        sj, si, d = map(int, input().split())
        arr[si][sj] = d
        for di, dj in ((-1, -1), (-1, 0), (-1, 1), (1, -1), (1, 0), (1, 1), (0, -1), (0, 1)):
            s = []
            for k in range(1, N):
                ni, nj = si+di*k, sj+dj*k
                if 1 <= ni <= N and 1 <= nj <= N:
                    if arr[ni][nj] == 0:
                        break
                    elif arr[ni][nj] == d:  # 같은 돌일 경우
                        for ci, cj in s:
                            arr[ci][cj] = d
                        break
                    else:  # 다른 돌일 경우
                        s.append((ni, nj))
                else:
                    break

    bcnt = wcnt = 0
    for lst in arr:
        bcnt += lst.count(1)
        wcnt += lst.count(2)
    print(f'#{tc} {bcnt} {wcnt}')


