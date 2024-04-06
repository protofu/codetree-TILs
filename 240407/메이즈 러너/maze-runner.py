import sys
import copy
input = sys.stdin.readline

n, m, k = map(int, input().split())
maze = [[0] * (n+1)] + [[0] + list(map(int, input().split())) for _ in range(n)]
mir_maze = [[0] * (n+1) for _ in range(n+1)]
position = [list(map(int, input().split())) for _ in range(m)]
EXIT = list(map(int, input().split()))
# ------- 전처리 -------
sy, sx, d_line = 0, 0, 0
# 상 하 좌 우 순서
# dys, dxs = [-1, 1, 0, 0], [0, 0, -1, 1]
# distance = [0] * m
ans = 0
# --------------------

# 참가자들이 움직이는 함수
def canMove():
    global EXIT, ans
    # for i in range(m):
    #     y, x = position[i]
    #     if [y, x] == EXIT:
    #         continue
    #     d = abs(y - EXIT[0]) + abs(x - EXIT[1])
    #     can_move = False
    #     for dy, dx in zip(dys, dxs):
    #         ny, nx = y + dy, x + dx
    #         # 범위를 벗어난 경우
    #         if 1 > ny or ny > n or 1 > nx or nx > n:
    #             continue
    #         # 벽인 경우
    #         if maze[ny][nx] != 0:
    #             continue
    #         # 출구까지 거리 계산
    #         dist = abs(ny - ey) + abs(nx - ex)
    #         # 기존보다 거리가 멀 경우
    #         if d <= dist:
    #             continue
    #         # 위 조건으로 모두 걸려졌으면
    #         # 가까운 거리로 초기화
    #         d = dist
    #         po = [ny, nx]
    #         can_move = True
    #     # 움직일 수 있다면 각 값을 바꿔준다
    #     if can_move:
    #         position[i] = po
    #         distance[i] += 1
    # m명의 모든 참가자들에 대해 이동을 진행합니다.
    for i in range(m):
        # 이미 출구에 있는 경우 스킵합니다.
        if position[i] == EXIT:
            continue

        ty, tx = position[i]
        ey, ex = EXIT

        # 행이 다른 경우 행을 이동시켜봅니다.
        if ty != ey:
            ny, nx = ty, tx

            if ey > ny:
                ny += 1
            else:
                ny -= 1

            # 벽이 없다면 행을 이동시킬 수 있습니다.
            # 이 경우 행을 이동시키고 바로 다음 참가자로 넘어갑니다.
            if not maze[ny][nx]:
                position[i] = [ny, nx]
                ans += 1
                continue

        # 열이 다른 경우 열을 이동시켜봅니다.
        if tx != ex:
            ny, nx = ty, tx

            if ex > nx:
                nx += 1
            else:
                nx -= 1

            # 벽이 없다면 행을 이동시킬 수 있습니다.
            # 이 경우 열을 이동시킵니다.
            if not maze[ny][nx]:
                position[i] = [ny, nx]
                ans += 1
                continue
# 미로가 바뀌는 함수
def square():
    global EXIT, sy, sx, d_line
    ey, ex = EXIT
    # 가장 작은 정사각형부터 모든 정사각형을 만들어봅니다.
    for sz in range(2, n + 1):
        # 가장 좌상단 r 좌표가 작은 것부터 하나씩 만들어봅니다.
        for y1 in range(1, n - sz + 2):
            # 가장 좌상단 c 좌표가 작은 것부터 하나씩 만들어봅니다.
            for x1 in range(1, n - sz + 2):
                y2, x2 = y1 + sz - 1, x1 + sz - 1

                # 만약 출구가 해당 정사각형 안에 없다면 스킵합니다.
                if not (y1 <= ey and ey <= y2 and x1 <= ex and ex <= x2):
                    continue

                # 한 명 이상의 참가자가 해당 정사각형 안에 있는지 판단합니다.
                is_traveler_in = False
                for l in range(m):
                    ty, tx = position[l]
                    if y1 <= ty and ty <= y2 and x1 <= tx and tx <= x2:
                        # 출구에 있는 참가자는 제외합니다.
                        if not (ty == ey and tx == ex):
                            is_traveler_in = True

                # 만약 한 명 이상의 참가자가 해당 정사각형 안에 있다면
                # sx, sy, square_size 정보를 갱신하고 종료합니다.
                if is_traveler_in:
                    sx = x1
                    sy = y1
                    d_line = sz
                    return


    # 90도 회전시키기
def changeMaze():
    global EXIT
    for i in range(sy, sy+d_line):
        for j in range(sx, sx+d_line):
            # 회전 전 1 빼주기
            if maze[i][j]:
                maze[i][j] -= 1

    for i in range(sy, sy + d_line):
        for j in range(sx, sx + d_line):
            ny, nx = i - sy, j - sx
            ry, rx = nx, d_line - ny - 1
            # print(i, j, "->", ry+tmp[0], rx+tmp[1])
            mir_maze[ry+sy][rx+sx] = maze[i][j]

    for i in range(sy, sy + d_line):
        for j in range(sx, sx + d_line):
            maze[i][j] = mir_maze[i][j]
def ro_pa_ex():
    global EXIT

    # for i in range(m):
    #     y, x = position[i]
    #     if sy <= y and y < sy + d_line and sx <= x and x < sx + d_line:
    #         ny, nx = y - sy, x - sx
    #         ry, rx = nx, d_line - ny - 1
    #         position[i] = [ry + sy, rx + sx]
    #
    # ey, ex = EXIT
    # if sy <= ey and ey < sy + d_line and sx <= ex and ex < sx + d_line:
    #     ny, nx = ey - sy, ex - sx
    #     ry, rx = nx, d_line - ny - 1
    #     EXIT = [ry + sy, rx + sx]
    for i in range(m):
        ty, tx = position[i]
        # 해당 참가자가 정사각형 안에 포함되어 있을 때에만 회전시킵니다.
        if sy <= ty and ty < sy + d_line and sx <= tx and tx < sx + d_line:
            # Step 1. (sx, sy)를 (0, 0)으로 옮겨주는 변환을 진행합니다.
            oy, ox = ty - sy, tx - sx
            # Step 2. 변환된 상태에서는 회전 이후의 좌표가 (x, y) . (y, square_n - x - 1)가 됩니다.
            ry, rx = ox, d_line - oy - 1
            # Step 3. 다시 (sx, sy)를 더해줍니다.
            position[i] = [ry + sy, rx + sx]

        # 출구에도 회전을 진행합니다.
    ey, ex = EXIT
    if sy <= ey and ey < sy + d_line and sx <= ex and ex < sx + d_line:
        # Step 1. (sx, sy)를 (0, 0)으로 옮겨주는 변환을 진행합니다.
        oy, ox = ey - sy, ex - sx
        # Step 2. 변환된 상태에서는 회전 이후의 좌표가 (x, y) . (y, square_n - x - 1)가 됩니다.
        ry, rx = ox, d_line - oy - 1
        # Step 3. 다시 (sx, sy)를 더해줍니다.
        EXIT = [ry + sy, rx + sx]


for _ in range(k):
    canMove()
    # 모든 사람이 출구로 탈출했는지 판단합니다.
    is_all_escaped = True
    for i in range(m):
        if position[i] != EXIT:
            is_all_escaped = False

    # 만약 모든 사람이 출구로 탈출했으면 바로 종료합니다.
    if is_all_escaped:
        break
    square()
    changeMaze()
    ro_pa_ex()

print(ans)
print(*EXIT)