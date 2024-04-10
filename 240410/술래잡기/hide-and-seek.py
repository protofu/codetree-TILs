n, m, h, k = tuple(map(int, input().split()))
players = {}
for i in range(m):
    y, x, d = tuple(map(int, input().split()))
    players[i] = [y-1, x-1, d-1, True]
woods = [[0]*n for _ in range(n)]
for _ in range(h):
    y, x = tuple(map(int, input().split()))
    woods[y-1][x-1] = 1
answer = 0
dys, dxs = [0, -1, 0, 1], [1, 0, -1, 0]
opp = {0:2, 1:3, 2:0, 3:1}
tys, txs = [-1, 0, 1, 0], [0, 1, 0, -1]
e = n//2
ey, ex, ed = e, e, 0
max_cnt, cnt, flag, val = 1, 0, 0, 1
remain = 0
def in_range(y, x):
    return 0<=y and y<n and 0<=x and x<n

def x_range(ex, x, ed):
    nx = ex + txs[ed]*3
    return ex<=x<nx

def y_range(ey, y, ed):
    ny = ey + tys[ed]*3
    return ey<=y<ny

for w in range(1, k+1):
    # 플레이어 움직임
    for i in players:
        y, x, d, alive = players[i]
        if abs(ey-y)+abs(ex-x) <=3:
            ny, nx = y+dys[d], x+dxs[d]
            if in_range(ny, nx):
                if (ny, nx) != (ey, ex):
                    players[i] = [ny, nx, d, alive]
            else:
                d = opp[d]
                ny, nx = y+dys[d], x+dxs[d]
                if (ny, nx) != (ey, ex):
                    players[i] = [ny, nx, d, alive]
                else:
                    players[i] = [y, x, d, alive]

    # 술래 움직임
    cnt += 1
    ey, ex = ey+tys[ed], ex+txs[ed]
    if (ey, ex) == (0, 0):
        max_cnt, cnt, flag, val = n, 1, 1, -1
        ed = 2
    elif (ey, ex) == (e, e):
        max_cnt, cnt, flag, val = 1, 0, 0, 1
        ed = 0
    else:
        if max_cnt == cnt:
            cnt = 0
            ed = (ed+val)%4
            if flag == 0:
                flag = 1
            else:
                flag = 0
                max_cnt += val

    # 도망자 잡기
    person = 0
    for i in players:
        y, x, d, alive = players[i]
        if alive:
            if ey==y and x_range(ex, x, ed) and not woods[y][x]:
                alive = False
                person+=1
                remain += 1
            elif ex==x and y_range(ey, y, ed) and not woods[y][x]:
                alive = False
                person+=1
                remain += 1
        players[i] = [y, x, d, alive]
    answer += person*w
    if remain == m:
        break
print(answer)