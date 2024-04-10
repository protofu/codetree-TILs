n, m, h, k = tuple(map(int, input().split()))
catcher = [n//2, n//2, 0]
players = {}
for i in range(m):
    y, x, d = tuple(map(int, input().split()))
    # 1은 좌우(0), 2는 상하(1)
    players[i] = [y-1, x-1, d-1, True]
dys, dxs = [0, 1, 0, -1], [1, 0, -1, 0]
opp = {0:1, 1:0, 2:3, 3:2}
woods = [[0]*n for _ in range(n)]
for _ in range(h):
    y, x = tuple(map(int, input().split()))
    woods[y-1][x-1] = 1
answer = 0
nail_y, nail_x = [-1, 0, 1, 0], [0, 1, 0, -1]
mx_cnt, cnt, flag, val = 1, 0, 0, 1


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
        ey, ex, ed = catcher
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
    cnt += 1
    ey, ex, ed = catcher
    ey, ex = ey+nail_y[ed], ex+nail_x[ed]
    if (ey, ex) == (0, 0):
        mx_cnt, cnt, flag, val = n, 1, 1, -1
        ed = 2
    elif (ey, ex) == (n//2, n//2):
        mx_cnt, cnt, flag, val = 1, 0, 0, 1
        ed = 0
    else:
        if cnt == mx_cnt:
            cnt = 0
            ed = (ed + val) % 4
            if flag == 0:
                flag = 1
            else:
                flag = 0
                mx_cnt += val
    catcher = ey, ex, ed

    ey, ex, ed = catcher
    person = 0
    for i in players:
        y, x, d, alive = players[i]
        # 나무가 없으며 살아있는 경우
        if woods[y][x]==0 and isAlive(i):
            # y 값이 같고, 3칸 안에 있는 경우
            if ey == y and enemy_x_range(ex, x, ed):
                players[i][3] = False
                person += 1
            # x 값이 같고, 3칸 안에 있는 경우
            elif ex == x and enemy_y_range(ey, y, ed):
                players[i][3] = False
                person += 1

    answer += ((w+1)*person)

print(answer)