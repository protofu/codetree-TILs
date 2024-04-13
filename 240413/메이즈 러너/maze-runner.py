n ,m, k = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(n)]
rlt = {}
ans = 0
alive = set()
player = {}
change = []
for i in range(1, m+1):
    y, x = map(int, input().split())
    player[i] = [y-1, x-1]
    rlt[i] = 0
    alive.add(i)
ey, ex = map(int, input().split())
ey -= 1
ex -= 1
# 우선순위  상하우좌
dys, dxs = [-1, 1, 0, 0], [0, 0, 1, -1]

r, c, size = 11, 11, 10

def init():
    global change
    change = []
def in_range(y, x):
    return 0<=y and y<n and 0<=x and x<n
def distance(y, x, ey, ex):
    return abs(y-ey)+abs(x-ex)
def move():
    for i in player:
        # 탈출했다면 pass
        if i not in alive: continue
        y, x = player[i]
        dist = distance(y, x, ey, ex)
        for dy, dx in zip(dys, dxs):
            ny, nx = y+dy, x+dx
            if not in_range(ny, nx): continue       # 범위를 벗어난다면 pass
            if maze[ny][nx] > 0: continue           # 벽이라면 pass
            if distance(ny, nx, ey, ex) >= dist: continue # 가까워지지 않는다면 pass
            player[i] = [ny, nx]
            rlt[i] += 1
            break
    for i in player:
        if i not in alive: continue
        y, x = player[i]
        if y==ey and x==ex:
            alive.remove(i)
def turn():
    global ey, ex, r, c, size
    # 출구와 참가자의 거리가 가장 짧은 사각형 구하기.
    r, c, size = 11, 11, 10
    # 사각형은 항상 정사각형
    for i in range(n-1):
        for j in range(n-1):
            for ei in range(i+1,n):
                for ej in range(j+1, n):
                    if ei-i != ej-j: continue       # 직사각형은 pass
                    for p in player:
                        if p not in alive: continue
                        y, x = player[p]
                        if i>y or j>x or ei<y or ej<x: continue
                        if i>ey or j>ex or ei<ey or ej<ex: continue
                        if ei-i >= size: continue
                        r, c, size = i, j, ei-i
    size += 1
    tmp = [[0]*size for _ in range(size)]
    spin = [[0]*size for _ in range(size)]
    # 해당 구역 미로 복사
    # print(r, r+size)
    for i in range(r, r+size):
        for j in range(c, c+size):
            if maze[i][j]>0:
                maze[i][j]-=1
            tmp[i-r][j-c] = maze[i][j]
            spin[i-r][j-c] = maze[i][j]
    for i in range(size):
        for j in range(size):
            tmp[j][(size-i-1)%size] = spin[i][j]

    for i in range(r, r+size):
        for j in range(c, c+size):
            maze[i][j] = tmp[i-r][j-c]
def chang():
    global ey, ex
    for i in player:
        if i not in alive: continue
        y, x = player[i]
        if r<=y and y<r+size and c<=x and x<c+size:
            ny, nx = y-r, x-c
            ry, rx = nx, size-ny-1
            player[i] = [ry+r, rx+c]
    if r <= ey and ey < r + size and c <= ex and ex < c + size:
        ny, nx = ey - r, ex - c
        ry, rx = nx, size - ny - 1
        ey, ex = ry + r, rx + c

for i in range(k):
    init()
    # 참가자가 이동하는 동작
    move()
    # 미로 회전 동작
    turn()
    # 출구 참가자 변환
    chang()
for i in rlt:
    ans += rlt[i]
print(ans)