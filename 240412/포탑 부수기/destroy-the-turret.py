# n 세로, m 가로, k 턴
n, m, k = map(int, input().split())
game = [list(map(int, input().split())) for _ in range(n)]
visit = [[0]*m for _ in range(n)]
# 우선순위 우 하 좌 상
dys, dxs = [0, 1, 0, -1], [1, 0, -1, 0]
dir = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
get_attack = [[0]*m for _ in range(n)]
def __init__():
    for i in range(n):
        for j in range(m):
            get_attack[i][j] = 0
def selectAttacker():
    # 공격자를 넣을 변수
    y, x, power, vis = -1, -1, 5001, 0
    # 가장 약한 포탑 선정
    for i in range(n):
        for j in range(m):
            # 부서진 포탑이라면 패스
            if game[i][j] == 0: continue
            # 저장된 값보다 약한 포탑은 넣기
            if game[i][j] < power:
                y, x, power, vis = i, j, game[i][j], visit[i][j]
            # 같다면
            elif game[i][j] == power:
                # 최근에 공격한 포탑이 승자
                if vis < visit[i][j]:
                    y, x, power, vis = i, j, game[i][j], visit[i][j]
                # 둘다 0인 상태라면
                elif vis == visit[i][j]:
                    # 행+열이 큰값이 선택
                    if i+j > y+x:
                        y, x, power, vis = i, j, game[i][j], visit[i][j]
                    # 행+열이 같다면, 열이 큰값
                    elif i+j == y+x and i > y:
                        y, x, power, vis = i, j, game[i][j], visit[i][j]
    # 선정된 포탑은 해당턴에 공격했다는 표시, 공격력 높여주기
    visit[y][x] = k
    game[y][x] += n+m

    return y, x
def attack(sy, sx):
    # 피해자를 넣을 함수
    y, x, power, vis = -1, -1, 0, 0
    # 가장 약한 포탑 선정
    for i in range(n):
        for j in range(m):
            # 자기 자신은 패스
            if i==sy and j==sx: continue
            # 부서진 포탑이라면 패스
            if game[i][j] == 0: continue
            # 저장된 값보다 강한 포탑은 넣기
            if game[i][j] > power:
                y, x, power, vis = i, j, game[i][j], visit[i][j]
            # 같다면
            elif game[i][j] == power:
                # 공격한지 오래된 포탑이 승자
                if vis > visit[i][j]:
                    y, x, power, vis = i, j, game[i][j], visit[i][j]
                # 둘다 0인 상태라면
                elif vis == visit[i][j]:
                    # 행+열이 작은값이 선택
                    if i + j < y + x:
                        y, x, power, vis = i, j, game[i][j], visit[i][j]
                    # 행+열이 같다면, 열이 작은값
                    elif i + j == y + x and i < y:
                        y, x, power, vis = i, j, game[i][j], visit[i][j]
    return y, x
def laser(sy, sx, wy, wx):
    q=[]
    q.append((sy, sx))
    laser_visit = [[0] * m for _ in range(n)]
    laser_visit[sy][sx] = True
    road_x = [[0] * m for _ in range(n)]
    road_y = [[0] * m for _ in range(n)]
    can_laser = False
    while q:
        y, x = q.pop(0)
        if y == wy and x == wx:
            can_laser = True
            break
        for dy, dx in zip(dys, dxs):
            ny, nx = (n+y+dy)%n, (m+x+dx)%m
            if game[ny][nx] == 0 or laser_visit[ny][nx]:
                continue
            laser_visit[ny][nx] = True

            road_y[ny][nx] = y
            road_x[ny][nx] = x
            q.append((ny, nx))

    if can_laser:
        game[wy][wx] -= game[sy][sx]
        if game[wy][wx] < 0:
            game[wy][wx] = 0
        get_attack[wy][wx] = 1
        ny, nx = road_y[wy][wx], road_x[wy][wx]
        while not (ny==sy and nx==sx):
            game[ny][nx] -= game[sy][sx]//2
            if game[ny][nx] < 0:
                game[ny][nx] = 0
            get_attack[ny][nx] = 1
            ny, nx = road_y[ny][nx], road_x[ny][nx]
    return can_laser
def boob(sy, sx, wy, wx):
    game[wy][wx] -= game[sy][sx]
    if game[wy][wx] < 0:
        game[wy][wx] = 0
        get_attack[wy][wx] = 1

    for dy, dx in dir:
        ny, nx = (wy+dy+n)%n, (wx+dx+m)%m
        if game[ny][nx] == 0: continue
        if ny==sy and nx==sx: continue
        game[ny][nx] -= game[sy][sx]//2
        get_attack[ny][nx] = 1
def repair():
    for i in range(n):
        for j in range(m):
            if game[i][j] == 0: continue
            if get_attack[i][j] == 1: continue
            game[i][j] += 1


# 공격력이 0 이면 공격 불가. 벽판정
# k 턴 동안 진행
for i in range(1, k+1):
    # 전처리
    __init__()
    # 공격자 선정 함수
    sy, sx = selectAttacker()
    get_attack[sy][sx] = 1
    # 선정된 공격자 공격 함수
    wy, wx = attack(sy, sx)
    # 레이저 공격
    if not laser(sy, sx, wy, wx):
        boob(sy, sx, wy, wx)
    # 포탑 정비 함수
    repair()

ans = 0
for i in game:
    ans = max(ans, max(i))
print(ans)