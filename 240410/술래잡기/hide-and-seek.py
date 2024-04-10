import sys

# 좌우 움직임(오른쪽 시작), 상하 움직임(아래쪽 시작) 2가지 유형
# 도망자 먼저, 그 다음 술래 k번 반복
# 술래와 거리가 3이하인 도망자만 움직임(맨해튼 거리)
# 도망자 규칙
# 1. 격자를 벗어나지 않는경우
# 1.1. 술래가 있다면 움직이지 않는다.
# 1.2. 그 외의 경우는 움직인다.
# 2. 격자를 벗어나는 경우
# 2.1. 반대방향으로 1칸 움직인다.
# 2.2. 역시 술래가 없어야 한다.
# 3. 술래는 달팽이 모양으로 움직인다.(위 방향 시작, 시계방향)
# 끝에 다다르게 되면 다시 거꾸로 움직인다.
# 이동 후 방향에 있는 도망자를 모두 잡게된다.(3칸)
# 나무가 있는 칸은 들키지 않는다.
# 잡힌 도망자는 사라지고 턴*잡힌 수 로 점수를 얻는다.

n, m, h, k = tuple(map(int, input().split()))
catcher = [n//2, n//2, 0, 0, 0, 0]
players = {}
for i in range(m):
    y, x, d = tuple(map(int, input().split()))
    # 1은 좌우(0), 2는 상하(1)
    players[i] = [y-1, x-1, d-1, True]
dys, dxs = [0, 1, 0, -1], [1, 0, -1, 0]
opp = {0:2, 1:3}
woods = [[0]*n for _ in range(n)]
for _ in range(h):
    y, x = tuple(map(int, input().split()))
    woods[y-1][x-1] = 1
answer = 0
nail_y, nail_x = [-1, 0, 1, 0], [0, 1, 0, -1]
re_nail_y, re_nail_x = [0, 1, 0, -1], [-1, 0, 1, 0]
move_cnt = 1

def nail(w):
    global catcher, move_cnt
    y, x, nd, move, re, flag = catcher
    ny, nx = y+nail_y[nd], x+nail_x[nd]
    move += 1
    # 반대편에 닿으면
    if [ny, nx] == [0, 0]:
        re = 1
        nd = 0
        move_cnt = n
    # 방향은 모두 이동한 다음 바뀜
    if move == move_cnt:
        nd = (nd + 1) % 4
        move = 0
        flag += 1
    if flag == 2:
        move_cnt += 1
        flag = 0
    catcher = [ny, nx, nd, move, re, flag]

def re_nail(w):
    global catcher, move_cnt
    y, x, nd, move, re, flag = catcher
    ny, nx = y+re_nail_y[nd], x+re_nail_x[nd]
    if [ny, nx] == [n//2, n//2]:
        re = 0
        nd = 0
        move_cnt = 1
    else:
        move += 1
        # 방향은 모두 이동한 다음 바뀜
        if move == move_cnt:
            nd = (nd + 1) % 4
            move = 0
            move_cnt -= 1
            flag += 1
        if flag == 2:
            move_cnt += 1
            flag = 0
    catcher = [ny, nx, nd, move, re, flag]

def isAlive(i):
    return players[i][3]

def in_range(y, x):
    return 0<=y and y<n and 0<=x and x<n

def enemy_x_range(ex, x, ed):
    nx = ex + nail_x[ed]*3
    return ex <= x <nx

def enemy_y_range(ey, y, ed):
    ny = ey + nail_y[ed]*3
    return ey <= y <ny

for w in range(k):
    # 도망자가 움직이는 동작
    for i in players:
        y, x, d, alive = players[i]
        ey, ex, ed, move, re, flag = catcher
        # 거리가 3 이하인 경우만
        if abs(ey-y)+abs(ex-x) <=3 and isAlive(i):
            ny, nx = y+dys[d], x+dxs[d]
            # 갈수있는 길이라면
            if in_range(ny, nx):
                # 술래가 없다면
                if [ny, nx] != catcher:
                    players[i] = [ny, nx, d, alive]        # 값 업데이트
                else:
                    players[i] = [y, x, d, alive]
            # 격자 밖이라면
            else:
                d = opp[d]
                ny, nx = y+dys[d], x+dxs[d]
                if [ny, nx] != catcher:
                    players[i] = [ny, nx, d, alive]
                else:
                    players[i] = [y, x, d, alive]
    # 술래가 움직이는 동작
    ey, ex, ed, move, re, flag = catcher
    if re == 0:
        nail(w)
    elif re == 1:
        re_nail(w)
    ey, ex, ed, move, re, flag = catcher
    cnt = 0
    for i in players:
        y, x, d, alive = players[i]
        # 나무가 없으며 살아있는 경우
        if woods[y][x]==0 and isAlive(i):
            # y 값이 같고, 3칸 안에 있는 경우
            if ey == y and enemy_x_range(ex, x, ed):
                players[i][3] = False
                cnt += 1
            # x 값이 같고, 3칸 안에 있는 경우
            elif ex == x and enemy_y_range(ey, y, ed):
                players[i][3] = False
                cnt += 1

    answer += ((w+1)*cnt)

print(answer)