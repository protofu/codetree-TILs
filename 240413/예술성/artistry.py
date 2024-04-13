from collections import deque

n = int(input())
paint = [list(map(int, input().split())) for _ in range(n)]
visit = [[0]*n for _ in range(n)]
crs = [[0]*n for _ in range(n)]
center = n//2
groups = []
nums = []
ans = 0
dys, dxs = [-1, 0, 1, 0], [0, 1, 0, -1]

def init():
    global groups
    global crs
    global visit
    global nums
    for i in range(n):
        for j in range(n):
            visit[i][j] = 0
            crs[i][j] = 0
    groups = []
    nums = []
def in_range(y, x):
    return 0<=y and y<n and 0<=x and x<n
def bfs(sy, sx):
    q = deque()
    q.append((sy, sx))
    visit[sy][sx] = 1
    groups[-1].add((sy,sx))

    while q:
        y, x = q.popleft()
        for dy, dx in zip(dys, dxs):
            ny, nx = y+dy, x+dx
            if not in_range(ny,nx): continue
            if visit[ny][nx]: continue
            if paint[ny][nx] == paint[sy][sx]:
                q.append((ny, nx))
                visit[ny][nx] = 1
                groups[-1].add((ny, nx))
def cross():
    y, x = center, center
    # 십자가 반시계 방향 회전
    for i in range(n):
        for j in range(n):
            if y == i or x== j:
                crs[(n-1-j)%n][i] = paint[i][j]
def square(y, x):
    tmp = [[0]*center for _ in range(center)]
    # 각 사각형 시계방향 90도
    # 각 사각형 복사
    for i in range(y, y+center):
        for j in range(x, x+center):
            tmp[i-y][j-x] = paint[i][j]
    # 돌려서 넣기
    for i in range(0, center):
        for j in range(0, center):
            crs[j+y][(center-i-1)%center+x] = tmp[i][j]

for i in range(1, 5):

    init()
    # 그룹간의 점수 구하기
    for i in range(n):
        for j in range(n):
            if visit[i][j] == 0:
                groups.append(set())
                nums.append(paint[i][j])
                bfs(i, j)
    # 점수 계산
    cnt = len(nums)
    for i in range(0, cnt-1):
        for j in range(i+1, cnt):
            point = (len(groups[i]) + len(groups[j]))*nums[i]*nums[j]
            for ci, cj in groups[i]:
                for dy, dx in zip(dys, dxs):
                    ny, nx = ci+dy, cj+dx
                    if (ny, nx) in groups[j]:
                        ans+=point
    # 3회차는 돌릴필요 없음
    # 십자모양 90도 돌리기
    cross()
    # 나머지 4칸을 90도 돌리기
    square(0, 0)
    square(center+1, 0)
    square(0, center+1)
    square(center+1, center+1)

    for i in range(n):
        for j in range(n):
            paint[i][j] = crs[i][j]

print(ans)