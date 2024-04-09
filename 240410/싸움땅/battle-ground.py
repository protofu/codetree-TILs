import sys

input = sys.stdin.readline
# n*n으로 진행
# 기능 1
# 해당 칸에 player가 없다면 gun 이 있는지 확인 후 gun 획득
# 이미 gun이 있다면 더 쎈 gun을 획득 후 가지고 있던 gun은 해당칸에 버림
# 기능 2
# player가 있다면 fight
# 총 공격력은 gun + player, 만약 두 player의 합능력이 같다면 초기 능력치로
# 이긴 player는 abs(초기 능력치-gun)을 획득
# 진 player는 가진 gun을 해당 격자에 내려놓고 원래 방향대로 1칸 진행
# 만약 진행방향에 player가 있거나 범위 밖인 경우 오른쪽으로 90도씩 회전하여 player가 없는 칸으로 이동
# 이긴 player는 해당칸에 있는 총과 비교하여 가장 높은 gun 획득, 나머지는 버림

n, m, k = tuple(map(int, input().split()))
game = [list(map(int, input().split())) for _ in range(n)]
gun = [[[0]for _ in range(n)] for _ in range(n)]
position = [[0]*n for _ in range(n)]
players = {}
point = [0]*m
dys, dxs = [-1, 0, 1, 0], [0, 1, 0, -1]
opp = {0:2, 1:3, 2:0, 3:1}
for i in range(n):
    for j in range(n):
        if game[i][j] > 0:
            gun[i][j].append(game[i][j])

for i in range(1, m+1):
    # 방향은 0 ↑, 1 →, 2 ↓, 3 ←
    y, x, d, s = tuple(map(int, input().split()))
    # player의 정보 저장  및 초기 gun = 0 으로 설정
    players[i] = [y-1, x-1, d, s, 0, 0]
    position[y-1][x-1] = i

def in_range(y, x):
    return 0<=y and y<n and 0<=x and x<n

def leave(num, cy, cx, cd, cs, cg, cp):
    # 현 방향부터 90도씩 빈칸 찾기
    for i in range(4):
        ny, nx = cy+dys[(cd+i)%4], cx+dxs[(cd+i)%4]
        if in_range(ny, nx) and position[ny][nx] == 0:
            if len(gun[ny][nx]):
                mx = max(gun[ny][nx])
                cg = mx
                gun[ny][nx].remove(mx)
            # 정보 갱신
            position[ny][nx] = num
            players[num] = [ny, nx, (cd+i)%4, cs, cg, cp]
            return

for _ in range(k):
    # 번호순대로 처리
    for i in players:
        # 1. 한칸식 이동
        cy, cx, cd, cs, cg, cp = players[i]
        ny, nx = cy+dys[cd], cx+dxs[cd]
        if not in_range(ny, nx):
            cd = opp[cd]
            ny, nx = cy+dys[cd], cx+dxs[cd]
        position[cy][cx] = 0

        # 2.1. 빈칸인 경우, 쎈 총 획득
        if position[ny][nx] == 0:
            if len(gun[ny][nx]) > 0:
                mx = max(gun[ny][nx])
                if cg < mx:
                    if cg > 0:
                        gun[ny][nx].append(cg)
                    gun[ny][nx].remove(mx)
                    cg = mx
            position[ny][nx] = i
            players[i] = [ny, nx, cd, cs, cg, cp]

        # 2.2. 빈칸이 아닌 경우, 상대방이 있는 경우
        else:
            enemy = position[ny][nx]
            ey, ex, ed, es, eg, ep = players[enemy]
            if cs+cg>es+eg or (cs+cg==es+eg and cs>es):     # 내가 이긴 경우
                cp += (cs+cg)-(es+eg)
                # 진 사람은 총을 놓고 떠난다
                leave(enemy, ny, nx, ed, es, 0, ep)

                # 이긴 사람은 가장 강한 총을 얻는다
                if cg < eg:
                    if cg > 0:
                        gun[ny][nx].append(cg)
                    cg = eg
                else:
                    if eg>0:
                        gun[ny][nx].append(eg)
                position[ny][nx] = i
                players[i] = [ny, nx, cd, cs, cg, cp]
            else:
                ep += (es + eg) - (cs + cg)
                # 진 사람은 총을 놓고 떠난다
                leave(i, ny, nx, cd, cs, 0, cp)

                # 이긴 사람은 가장 강한 총을 얻는다
                if eg < cg:
                    if eg > 0:
                        gun[ny][nx].append(eg)
                    eg = cg
                else:
                    if cg > 0:
                        gun[ny][nx].append(cg)
                position[ny][nx] = enemy
                players[enemy] = [ey, ex, ed, es, eg, ep]

for i in players:
    print(players[i][5], end=' ')