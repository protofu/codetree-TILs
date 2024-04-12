# n격자크기, m팀 개수, k라운드
n, m, k = map(int, input().split())
game = [list(map(int, input().split())) for _ in range(n)]
team = [[0]*n for _ in range(n)]
visit = [[0]*n for _ in range(n)]
ORD = [[0]*n for _ in range(n)]
dys, dxs = [-1, 0, 1, 0], [0, 1, 0, -1]
score = {}
def init():
    for i in range(n):
        for j in range(n):
            ORD[i][j] = 0
            visit[i][j] = 0
def bfs():
    cnt = 1
    for i in range(n):
        for j in range(n):
            if game[i][j] == 1:
                # print(i, j)
                team[i][j] = cnt
                score[cnt] = 0
                q=[]
                q.append((i, j))
                while q:
                    y, x = q.pop()
                    for dy, dx in zip(dys, dxs):
                        ny, nx = y+dy, x+dx
                        if not in_range(ny, nx): continue
                        if team[ny][nx]: continue
                        if game[ny][nx]:
                            # print("q", q)
                            team[ny][nx] = cnt
                            q.append((ny, nx))
                cnt += 1
def in_range(y, x):
    return 0<=y and y<n and 0<=x and x<n
def move():
    check = set()
    for i in range(n):
        for j in range(n):
            if team[i][j] in check: continue
            if game[i][j] == 1:
                check.add(team[i][j])
                q=[]
                q.append((i, j))
                flag = 0
                while q:
                    y, x = q.pop()
                    tmp = game[y][x]
                    for dy, dx in zip(dys, dxs):
                        ny, nx = y+dy, x+dx
                        if not in_range(ny, nx): continue
                        if game[ny][nx] == 4:
                            if tmp == 2:
                                game[ny][nx] = 2
                                if game[y][x] == 2:
                                    game[y][x] = 4
                            elif tmp == 1:
                                game[ny][nx] = 1
                                game[y][x] = 4
                        elif game[ny][nx] == 3:
                            # 모두 연결이 된 경우
                            if tmp == 1:
                                flag = 1
                                game[ny][nx] = 1
                                game[y][x] = 4
                            else:
                                game[ny][nx] = 4
                                game[y][x] = 3
                        elif game[ny][nx] == 2:
                            q.append((ny, nx))
                    if flag:
                        for dy, dx in zip(dys, dxs):
                            ny, nx = y + dy, x + dx
                            if not in_range(ny, nx): continue
                            if game[ny][nx] == 4:
                                game[ny][nx] = 3
                                break
def oRD():
    for i in range(n):
        for j in range(n):
            if game[i][j] == 1:
                c = 1
                ORD[i][j] = c
                q = []
                q.append((i, j))
                while q:
                    c+=1
                    y, x = q.pop(0)
                    for dy, dx in zip(dys, dxs):
                        ny,nx=y+dy,x+dx
                        if not in_range(ny, nx): continue
                        if ORD[ny][nx]:continue
                        if game[ny][nx]==2 or game[ny][nx]==3:
                            ORD[ny][nx] = c
                            q.append((ny, nx))
def ball(round):
    dir, num = (round//n)%4, round%n
    dy, dx, val_y, val_x = 0, 0, 0, 0
    if dir == 0:
        dy = num
        val_x = 1
    elif dir == 1:
        dy = n-1
        dx =num
        val_y = -1
    elif dir == 2:
        dy = n - num - 1
        dx = n-1
        val_x = -1
    elif dir == 3:
        dx = n - num - 1
        val_y = 1
    ry, rx = 0, 0
    for i in range(n):
        ny, nx = dy+val_y*i, dx+val_x*i
        if 1<=game[ny][nx]<=3:
            # 점수 추가
            score[team[ny][nx]] += ORD[ny][nx] * ORD[ny][nx]
            ry, rx = ny, nx
            break
    q = []
    q.append((ry, rx))
    thr_y, thr_x = 0, 0
    fir_y, fir_x = 0, 0
    if game[ry][rx] == 1:
        fir_y, fir_x = ry, rx
    elif game[ry][rx] == 3:
        thr_y, thr_x = ry, rx
    while q:
        sy, sx = q.pop()
        for dy, dx in zip(dys, dxs):
            y, x = sy+dy, sx+dx
            if not in_range(y, x) or game[y][x] == 4: continue
            if visit[y][x]: continue
            if game[y][x] == 1:
                fir_y, fir_x = y, x
                visit[y][x] = 1
            elif game[y][x] == 3:
                thr_y, thr_x = y, x
                visit[y][x] = 1
            elif game[y][x] == 2:
                visit[y][x] = 1
                q.append((y, x))
    game[fir_y][fir_x] = 3
    game[thr_y][thr_x] = 1

bfs()
for round in range(k):
    init()
    # 머리 사람을 따라 이동하는 동작
    # print("이전")
    # for i in game:
    #     print(i)
    move()
    # print("이후")
    # for i in game:
    #     print(i)
    oRD()
    # 공이 던져지는 동작
    ball(round)

# print(score)
ans = 0
for i in score:
    ans += score[i]
print(ans)