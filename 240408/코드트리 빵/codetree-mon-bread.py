import sys

input = sys.stdin.readline

n, m = tuple(map(int, input().split()))
board = [[0]*(n+1)] + [[0] + list(map(int, input().split())) for _ in range(n)]
visit = [[0]*(n+1) for _ in range(n+1)]
conv = [tuple(map(int, input().split())) for _ in range(m)]
base = []
people = []
distance = []
arrive_cnt = [0]*m
# print(n, m)
# for i in board:
#     print(i)
# print(person)

# 전처리
per = -1
dys, dxs = [-1, 0, 0, 1], [0, -1, 1, 0]
for i in range(1, n+1):
    for j in range(1, n+1):
        if board[i][j]:
            base.append((i, j))
# print("편의점", conv)
# print("베이스", base)

# ----------------------------------------
# 베이스 찾고, people에 도착한 사람 저장
def find_base(per):
    # 해당 편의점 좌표 저장
    cy, cx = conv[per]
    # 베이스 캠프 중 가장 가까운, 맨해튼 거리
    dist = 31
    py, px = 0, 0
    # 베이스를 돌며 확인
    for i in range(len(base)):
        by, bx = base[i]
        # 이미 차지한 베이스는 패스
        if visit[by][bx]:
            continue
        l = abs(by-cy) + abs(bx-cx)
        if dist < l:
            continue
        # 만약 거리가 같다면
        elif dist == l:
            # 행이 작은걸로
            if py > by:
                py, px = by, bx
            # 행이 같다면 열이 작은걸로
            elif py == by and px > bx:
                py, px = by, bx
        else:
            dist = l
            py, px = by, bx
    visit[py][px] = 1
    people.append((py, px))
    distance.append(l)
# 시간마다 사람이 움직이는 함수
def move():
    global per
    # 베이스에 도착한 사람을 돌면서
    for i in range(len(people)):
        sy, sx = people[i]
        # 해당턴에 베이스를 찍었다면 패스
        if i == per:
            continue
        # 도착했다면 패스
        if people[i] == conv[i]:
            continue
        for j in range(4):
            ny, nx = sy+dys[j], sx+dxs[j]
            l = abs(ny-conv[i][0]) + abs(nx-conv[i][1])
            # 벗어나거나 가면 안될곳이면 패스
            if ny < 1 or ny > n or nx < 1 or nx > n or visit[ny][nx]:
                continue
            # 거리가 늘어난다면 패스
            if distance[i] <= l:
                continue
            people[i] = (ny, nx)
            distance[i] = l
            break
# 사람이 편의점에 도착했는지 체크
def isArrive():
    global arrive_cnt
    for i in range(len(people)):
        py, px = people[i]
        if not arrive_cnt[i] and people[i] == conv[i]:
            visit[py][px] = 1
            arrive_cnt[i] = 1
    if sum(arrive_cnt) == m:
        return True
    return False

# 1. 베이스 캠프에 들어가는 동작 -> 좌표가 밝혀짐. visit에 체크
# 2. 최단거리로 움직이는 동작 -> dys, dxs를 이용해서 좌표이동
# 3. 편의점에 도착한지 체크, 도착했다면 visit에 체크

while True:
    per += 1
    # 베이스를 밟는 동작
    if per < m:
        find_base(per)
        # print("위치", people)

    # 첫번째 턴은 그냥 넘기기
    if per < 1:
        continue
    move()
    # 모두가 도착했다면 끝
    if isArrive():
        break
    # print("시간과 현 위치", per+1, people)
print(per+1)