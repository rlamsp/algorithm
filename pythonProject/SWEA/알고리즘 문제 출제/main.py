from collections import deque

# 델타 탐색
dx = [0, -1, 1, 0]
dy = [-1, 0, 0, 1]


# bfs알고리즘을 바탕으로 작성
def bfs(e):
    q = deque([e[0]])  # deque를 사용
    visited = [[0 for _ in range(N)] for _ in range(N)]  # 방문 체크
    visited[e[0][0]][e[0][1]] = 0  # 현재 위치를 visited에 넣음
    check_order = []
    while q:
        tmp = q.popleft()
        for i in range(4):  # 델타 탐색
            tmp_x = tmp[1] + dx[i]
            tmp_y = tmp[0] + dy[i]
            if 0 <= tmp_x < N and 0 <= tmp_y < N:  # 범위 내에서
                if visited[tmp_y][tmp_x] == 0 and (
                        prob[tmp_y][tmp_x] == e[1] or prob[tmp_y][tmp_x] == 0):  # 방문하지 않은 곳 중에 지나갈 수 있는 곳이면
                    q.append([tmp_y, tmp_x])  # 지나가면서 q에 저장
                    visited[tmp_y][tmp_x] = 1 + visited[tmp[0]][tmp[1]]
                if 0 < prob[tmp_y][tmp_x] < e[1]:  # 풀수 있는 문제가 있는 곳이면
                    if visited[tmp_y][tmp_x] == 0:
                        visited[tmp_y][tmp_x] = 1 + visited[tmp[0]][tmp[1]]
                        check_order.append([tmp_y, tmp_x, visited[tmp_y][tmp_x]])  # 위치와 해당 위치까지의 거리를 저장
                        q.append([tmp_y, tmp_x])

    if check_order:  # 풀 수 있는 문제가 있으면
        check_order.sort(key=lambda x: (x[2], x[0], x[1]))  # 시간순, 위에 있는 순, 왼쪽에 있는 순으로 정렬한다
        return [check_order[0][:2], visited[check_order[0][0]][check_order[0][1]]]  # 해당 문제의 위치와 시간을 리턴한다
    return -1


N, K, M = map(int, input().split())

prob = [list(map(int, input().split())) for _ in range(N)]
prob_size = [[] for _ in range(7)]
start = [[0, 0], 2]  # [시작위치],현재 실력
for i in range(N):
    for j in range(N):
        for k in (1, 2, 3, 4, 5, 6, 9):
            if prob[i][j] == 9:
                start[0] = [i, j]  # 시작 위치 지정
            elif prob[i][j] == k:
                prob_size[k].append([i, j])
solve_time = 0
check = False
for i in range(2, 8):  # 2에서부터 시작해서
    start[1] = i  # 실력을 늘려서
    if start[1] == M:  # 실력이 목표에 도달했다면 종료한다
        break
    solved_problem = 0  # 해당 실력에서 푼 문제수를 초기화
    while solved_problem < i <= 7 and not check and solve_time <= K:  # 제한 시간내에 문제를 덜 풀었다면 반복해서 푼다
        a = bfs(start)
        if a != -1:  # 풀 문제가 있으면
            prob[start[0][0]][start[0][1]] = 0
            start[0] = a[0][:]
            solved_problem += 1
            print(solve_time)
            solve_time += a[1] + prob[a[0][0]][a[0][1]] * 2
            prob[a[0][0]][a[0][1]] = 9

        else:  # 풀 문제가 없으면
            check = True
    if check:
        break
if start[1] == M and K >= solve_time:
    print(f'성공!\n{solve_time}')
else:
    print('실패')
