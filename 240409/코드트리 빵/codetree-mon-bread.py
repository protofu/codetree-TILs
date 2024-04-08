import sys
from collections import deque
input = sys.stdin.readline
INT_MAX = sys.maxsize
EMPTY = (-1, -1)

n, m = tuple(map(int, input().split()))
board = [list(map(int, input().split())) for _ in range(n)]
visit = [[0]*n for _ in range(n)]
conv = []
for _ in range(m):
    y, x = tuple(map(int, input().split()))
    conv.append((y-1, x-1))
people = [EMPTY] * m
step = [[0]*n for _ in range(n)]
# print(n, m)
# for i in board:
#     print(i)
# print(person)

# 전처리
per = 0
dys, dxs = [-1, 0, 0, 1], [0, -1, 1, 0]

# print("편의점", conv)
# print("베이스", base)

# ----------------------------------------
# 최단거리를 구하는 함수
def bfs(point):
    for i in range(n):
        for j in range(n):
            visit[i][j] = False
            step[i][j] = 0

    q = deque()
    q.append(point)
    sy, sx = point
    visit[sy][sx] = 1
    step[sy][sx] = 0

    while q:
        y, x = q.popleft()

        for dy, dx in zip(dys, dxs):
            ny, nx = y + dy, x + dx
            if can_go(ny, nx):
                visit[ny][nx] = True
                step[ny][nx] = step[y][x] + 1
                q.append((ny, nx))

def in_range(y, x):
    return 0 <= x and x < n and 0 <= y and y < n

def can_go(y, x):
    return in_range(y, x) and not visit[y][x] and board[y][x] != 2
# 1. 베이스 캠프에 들어가는 동작 -> 좌표가 밝혀짐. visit에 체크
# 2. 최단거리로 움직이는 동작 -> dys, dxs를 이용해서 좌표이동
# 3. 편의점에 도착한지 체크, 도착했다면 visit에 체크
def sim():
    for i in range(m):
        if people[i] == EMPTY or people[i] == conv[i]:
            continue

        bfs(conv[i])
        py, px = people[i]
        min_dist = INT_MAX
        min_y, min_x = -1, -1
        for dy, dx in zip(dys, dxs):
            ny, nx = py + dy, px + dx
            if in_range(ny, nx) and visit[ny][nx] and min_dist > step[ny][nx]:
                min_dist = step[ny][nx]
                min_y, min_x = ny, nx

        people[i] = (min_y, min_x)

    for i in range(m):
        if people[i] == conv[i]:
            py, px = people[i]
            board[py][px] = 2

    if per > m:
        return

    bfs(conv[per-1])
    min_dist = INT_MAX
    min_y, min_x = -1, -1
    for i in range(n):
        for j in range(n):
            if visit[i][j] and board[i][j] == 1 and min_dist > step[i][j]:
                min_dist = step[i][j]
                min_y, min_x = i, j
    people[per-1] = (min_y, min_x)
    board[min_y][min_x] = 2

def end():
    for i in range(m):
        if people[i] != conv[i]:
            return False
    return True

while True:
    per += 1
    sim()
    if end():
        break
print(per)