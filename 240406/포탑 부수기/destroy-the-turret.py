import sys
# sys.setrecursionlimit(10**3)
input = sys.stdin.readline
N, M, K = map(int, input().split())
game = [list(map(int, input().split())) for _ in range(N)]
count = [[0] * M for _ in range(N)]

def attacker(): # 공격자 선정 함수
    tmp = [5001, 0, 0, 1001]
    for y in range(N):
        for x in range(M):
            # 공격력이 가장 낮은.
            if tmp[0] > game[y][x] and game[y][x] != 0:
                tmp = [game[y][x], y, x, count[y][x]]
            # 만약 같다면
            elif tmp[0] == game[y][x]:
                # 가장 최근에 공격한
                if tmp[3] < count[y][x]:
                    tmp = [game[y][x], y, x, count[y][x]]
                # 둘다 공격한 적이 없다면, 열+행 큰값
                elif tmp[3] == count[y][x] and sum(tmp[1:3]) < (y+x):
                    tmp = [game[y][x], y, x, count[y][x]]
                # 둘다 공격한 적이 없다면, 열+행이 같다면, 열이 높은
                elif tmp[3] == count[y][x] and sum(tmp[1:3]) < (y+x) and tmp[2] < x:
                    tmp = [game[y][x], y, x, count[y][x]]
    return tmp

def reciver(ny, nx): # 공격자 제외 가장 강한 적을 뽑는 함수
    re_tmp = [0, 0, 0, 1001]
    for y in range(N):
        for x in range(M):
            # 자신을 제외
            if [y, x] == [ny, nx] or game[y][x] == 0:
                pass
            else: # 자신이 선택된걸 제외
                # 공격력이 가장 높은.
                if re_tmp[0] < game[y][x]:
                    re_tmp = [game[y][x], y, x, count[y][x]]
                elif re_tmp[0] == game[y][x]:
                    # 공격한지 오래된 포탑
                    if re_tmp[3] > count[y][x]:
                        re_tmp = [game[y][x], y, x, count[y][x]]
                    # 행과 열의 합이 가장 작은
                    elif re_tmp[3] == count[y][x] and sum(re_tmp[1:3]) > (y + x):
                        re_tmp = [game[y][x], y, x, count[y][x]]
                    # 열이 가장 작은
                    elif sum(re_tmp[1:3]) == (y + x) and re_tmp[2] > x:
                        re_tmp = [game[y][x], y, x, count[y][x]]
    return re_tmp

def laser(ay, ax, ry, rx, visit):
    dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
    if [ay, ax] == [ry, rx]:
        return True
    else:
        for i in range(4):
            ny, nx = ay + dy[i], ax + dx[i]
            if 0>ny:
                ny = N+ny
            elif N<=ny:
                ny = N-ny
            if 0>nx:
                nx = N+nx
            elif N<=nx:
                nx = N-nx
            if game[ny][nx] != 0 and not visit[ny][nx]:
                visit[ny][nx] = 1
                laser(ny, nx, ry, rx, visit)
                if visit[ry][rx]:
                    return True
                else:
                    visit[ny][nx] = 0
    return False

def attack(ay, ax, ry, rx): # 공격 함수(레이저, 포탄)
    visit = [[0] * M for _ in range(N)]
    take_attack = [[0] * M for _ in range(N)]
    take_attack[ay][ax] = 1
    take_attack[ry][rx] = 1
    game[ay][ax] += (N+M)
    # 레이저 공격
    if laser(ay, ax, ry, rx, visit):
        game[ry][rx] -= game[ay][ax]
        if game[ry][rx] < 0:
            game[ry][rx] = 0
        for i in range(N):
            for j in range(M):
                if visit[i][j] and [i, j] != [ry, rx]:
                    take_attack[i][j] = 1
                    game[i][j] -= game[ay][ax]//2
    # 포탄 공격
    else:
        game[ry][rx] -= game[ay][ax]
        if game[ry][rx] < 0:
            game[ry][rx] = 0
        dy, dx = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]
        for i in range(8):
            by, bx = ry + dy[i], rx + dx[i]
            if 0>by:
                by = N+by
            elif N<=by:
                by = N-by
            if 0>bx:
                bx = N+bx
            elif N<=bx:
                bx = N-bx
            if game[by][bx] != 0:
                game[by][bx] -= game[ay][ax]//2
                take_attack[by][bx] = 1
                if game[by][bx] < 0:
                    game[by][bx] = 0
    for i in range(N):
        for j in range(M):
            if game[i][j] != 0 and take_attack[i][j] == 0:
                game[i][j] += 1

def strong():
    big = 0
    for line in game:
        if max(line) > big:
            big = max(line)
    return big

for i in range(K):
    canon = attacker() # [공격력, y, x]
    count[canon[1]][canon[2]] = i+1
    # print("공격 캐논", canon)
    enemy = reciver(canon[1], canon[2]) # [공격력, y, x, 공격 순서]
    # print("공격 대상", enemy)
    attack(canon[1], canon[2], enemy[1], enemy[2])
    # print("---------", i+1, "차 공격 -----------")
    # for i in game:
    #     print(i)
    cnt = 0
    for i in game:
        for j in i:
            if j > 0:
                cnt += 1
    if cnt <= 1:
        break
answer = strong()
print(answer)