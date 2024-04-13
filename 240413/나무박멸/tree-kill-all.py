# n격자, m년수, k제초제 확산범위, c 제초제 남은 년수
n, m, k, c = map(int, input().split())
woods = [list(map(int, input().split())) for _ in range(n)]
empty = [[0]*n for _ in range(n)]
woods_here = []
kill = [[0]*n for _ in range(n)]
die_tree = 0
dys, dxs = [-1, 0, 1, 0], [0, 1, 0, -1]
kys, kxs = [-1, -1, 1, 1], [-1, 1, 1, -1]
def init():
    global woods_here
    for i in range(n):
        for j in range(n):
            empty[i][j] = 0
            # 제초제 효과 1년씩 줄어드는 기능
            if kill[i][j] > 0:
                kill[i][j] -=1

    woods_here = []
def in_range(y, x):
    return 0<=y and y<n and 0<=x and x<n
def grow():
    for i in range(n):
        for j in range(n):
            trees, emp = 0, 0
            # 나무가 있을 경우
            if woods[i][j] > 0:
                woods_here.append((i, j))
                for dy, dx in zip(dys, dxs):
                    ny, nx = i+dy, j+dx
                    if not in_range(ny, nx): continue
                    if woods[ny][nx] > 0: trees+=1
                    if woods[ny][nx] == 0 and kill[ny][nx] == 0: emp+=1
                woods[i][j] += trees
                empty[i][j] = emp
def spread():
    for i, j in woods_here:
        if empty[i][j] > 0:
            for dy, dx in zip(dys, dxs):
                ny, nx = i+dy, j+dx
                if not in_range(ny, nx): continue   # 범위밖 제외
                if woods[ny][nx]<0: continue        # 벽인경우 제외
                if kill[ny][nx] >0: continue        # 제초제 상태인 경우 제외
                if (ny,nx) in woods_here: continue  # 원래 나무가 있던 경우 제외
                woods[ny][nx] += woods[i][j]//empty[i][j]
def kill_tree():
    global die_tree
    most_kill, gy, gx = 0, 0, 0
    for i in range(n):
        for j in range(n):
            if woods[i][j] > 0:
                cnt = woods[i][j]
                for ky, kx in zip(kys, kxs):
                    ny, nx = i + ky, j + kx
                    times = 0
                    while times != k:
                        times+=1
                        if not in_range(ny,nx): break
                        if woods[ny][nx]<=0:break
                        if woods[ny][nx] > 0:
                            cnt += woods[ny][nx]
                        ny, nx = ny+ky, nx+kx
                if most_kill<cnt:
                    most_kill = cnt
                    gy, gx = i, j
                elif most_kill == cnt and gy > i:
                    most_kill = cnt
                    gy, gx = i, j
                elif most_kill == cnt and gy == i and gx > j:
                    most_kill = cnt
                    gy, gx = i, j
    # 해당 자리에 제초제 뿌리기
    die_tree += woods[gy][gx]
    kill[gy][gx] = c+1
    if woods[gy][gx] > 0:
        woods[gy][gx] = 0
        # print(gy,gx)
        # 제초제를 뿌리는 동작
        for ky, kx in zip(kys, kxs):
            ny, nx = gy + ky, gx + kx
            times = 0
            while times != k:
                times += 1
                if not in_range(ny, nx): break
                if woods[ny][nx] <= 0:
                    kill[ny][nx] = c + 1
                    break
                elif woods[ny][nx] > 0:
                    die_tree+=woods[ny][nx]
                    kill[ny][nx] = c+1
                    woods[ny][nx] = 0
                ny, nx = ny + ky, nx + kx




for round in range(m):
    # print(round, "라운드 현황__________________")
    # 만약 나무가 없다면 끝
    flag = False
    for i in range(n):
        for j in range(n):
            if woods[i][j] > 0:
                flag = True
                break
    if not flag:
        break
    # empty 리스트 초기화
    init()
    # 나무 성장, 빈칸 세기
    grow()
    # print("성장")
    # for i in woods:
    #     print(i)
    # 나무 번식 (제초제가 없는)
    spread()
    # print("번식")
    # for i in woods:
    #     print(i)
    # 제초제 뿌리기 (가장 많이 죽는곳)
    kill_tree()
    # print("제초제 현황")
    # for i in kill:
    #     print(i)
    # print("제초")
    # for i in woods:
    #     print(i)


print(die_tree)