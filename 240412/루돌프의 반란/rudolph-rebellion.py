# n 격자크기, m 턴횟수, p 산타갯수, c 루돌프 충동 점수, d 산타 충돌 점수
n, m, p, c, d = map(int, input().split())
dolph = list(map(int, input().split()))
santa = {}
lose_santa = set()
# 산타 - 상우하좌 - 좌하우상으로 탐색하자.
sys, sxs = [0, 1, 0, -1], [-1, 0, 1, 0]
opp = {0:2, 1:3, 2:0, 3:1}
# 루돌프 - 8방향
dys, dxs = [-1, 1, 0, -1, 1, -1, 0, 1], [0, -1, 1, -1, 0, 1, -1, 1]
for _ in range(p):
    p, y, x = map(int, input().split())
    # y, x, stun, point
    santa[p] = [y, x, 0, 0]

santa = dict(sorted(santa.items(), key=lambda x: x[0]))

# 거리계산 함수
def distance(ey, ex, y, x):
    return (ey-y)**2 + (ex-x)**2
# 방향을 정하기
def dolph_dr(ey, ex, y, x):
    ny, nx = ey, ex
    d = 8
    if ey == y:
        if ex > x:      # 0, -1
            nx-=1
            d=6
        elif ex < x:    # 0, 1
            nx+=1
            d=2
    elif ex == x:
        if ey > y:      # -1, 0
            ny-=1
            d=0
        elif ey < y:    # 1, 0
            ny+=1
            d=4
    elif ey>y and ex>x: # -1, -1
        ny-=1
        nx-=1
        d=3
    elif ey<y and ex<x: # 1, 1
        ny+=1
        nx+=1
        d=7
    elif ey>y and ex<x: # -1, 1
        ny-=1
        nx+=1
        d=5
    elif ey<y and ex>x: # 1, -1
        ny+=1
        nx-=1
        d=1
    return ny, nx, d

def in_range(y, x):
    return 1<=y and y<=n and 1<=x and x<=n

# 해당 위치에 산타가 있을경우 True/ 없으면 False
def isSanta(y, x, cur):
    for idx in santa:
        # 탈락한 산타 및 자신 제외
        if idx in lose_santa or idx == cur:
            continue
        ry, rx, _, _ = santa[idx]
        if y==ry and x==rx:
            return True
    return False
# print("산타", santa[idx])
# 산타 연쇄 충돌 반응
def push_santa(start, dir, dys, dxs, val, ey, ex):
    q = []
    q.append(start)
    while q:
        now = q.pop(0)
        y, x, _, _ = santa[now]
        for idx in santa:
            # 탈락한 산타는 제외
            if idx in lose_santa or idx == now:
                continue
            sy, sx, s_stun, s_point = santa[idx]
            # 충돌했다면 거리 업데이트, 범위 체크, 안이라면 q에 넣기
            if (y, x) == (sy, sx):
                ny, nx = sy + dys[dir] * val, sy + dxs[dir] * val
                if in_range(ny, nx):
                    # 루돌프랑 박았다면
                    if ny==ey and nx==ex:
                        print("!!!!!", santa[idx])
                        santa[idx] = [ny, nx, s_stun, s_point+c]
                        print("!!!!!", santa[idx])
                    else:
                        santa[idx] = [ny, nx, s_stun, s_point]
                        q.append(idx)
                # 범위 밖이라면 탈락
                else:
                    lose_santa.add(idx)

for k in range(1, m+1):
    # 루돌프의 움직임
    close_santa = 0
    dist = 2*(50**2)
    ey, ex = dolph
    # 가장 가까운 산타를 탐색하는 동작
    for cur in santa:
        # 탈락한 산타가 아니라면.
        if cur not in lose_santa:
            y, x, _, _ = santa[cur]
            tmp = distance(ey, ex, y, x)
            # 거리가 더 짧다면 업데이트
            if dist > tmp:
                dist = tmp
                close_santa = cur
            # 거리가 같다면
            elif dist == tmp:
                wy, wx, _, _ = santa[close_santa]
                if wy < y:
                    close_santa = cur
                elif wy == y and wx < x:
                    close_santa = cur
    # print(k, "턴의 가까운", close_santa)
    # 루돌프가 이동하는 동작
    san_y, san_x, stun, point = santa[close_santa]
    # 루돌프의 이동
    ey, ex, dir = dolph_dr(ey, ex, san_y, san_x)
    # print(k, "턴의 방향" , dir)
    dolph = [ey, ex]
    # 충돌확인, 연쇄 반응
    # print(dolph)
    # 만약 충돌했다면 점수를 얻고
    now_stun=set()
    if (ey, ex) == (san_y, san_x):
        # c만큼 밀려남
        san_y, san_x = san_y+dys[dir]*c, san_x+dxs[dir]*c
        santa[close_santa] = [san_y, san_x, 1, point + c]
        now_stun.add(close_santa)
        # 벗어낫다면 탈락
        if not in_range(san_y, san_x):
            lose_santa.add(close_santa)
        # 범위 안이라면 연쇄반응 체크
        else:
            push_santa(close_santa, dir, dys, dxs, c, ey, ex)
    # 산타의 동작
    for idx in santa:
        # 이미 탈락했다면 패스
        if idx in lose_santa or idx in now_stun:
            if idx in now_stun:
                now_stun.remove(idx)
            continue
        y, x, stun, point = santa[idx]
        dir = 0
        # 기절 상태라면 stun-1 해주고 패스
        if stun > 0:
            santa[idx] = [y, x, stun-1, point]
            continue
        # 루돌프와 가까운 방향으로 진행, 돌프는 ey, ex인 상태임, 기존거리로 초기화
        tmp = distance(ey, ex, y, x)
        is_short = distance(ey, ex, y, x)
        # 가까운 거리를 체크, 상우하좌 니까 좌하우상 순서로 체크해서 업데이트하면 될것같음
        # 다른 산타가 있거나, 범위 밖이면 이동 불가.
        next_y, next_x = 0, 0
        for i in range(4):
            ny, nx = y+sys[i], x+sxs[i]
            # 해당 칸이 범위를 벗어나거나 산타가 있다면 경우 제외
            if in_range(ny, nx) and not isSanta(ny, nx, idx):
                # 기존 거리보다 단축되고, 탐색한 거리보다 짧다면 저장
                n_dist = distance(ey, ex, ny, nx)
                if tmp > n_dist and is_short >= n_dist:
                    is_short = n_dist
                    # 이때의 방향 저장해두기
                    next_y, next_x = ny, nx
                    dir = i
        # 위치의 변화가 없다면 패스
        if (next_y, next_x) == (0, 0):
            continue
        # 위치 변화가 있고, 그곳에 루돌프가 있다면, 점수 획득 후 밀려나기 및 연쇄반응
        elif (next_y, next_x) == (ey, ex):
            # 포인트 획득
            point+=d
            # 반대방향으로 산타의 밀려나기
            dir = opp[dir]
            next_y, next_x = next_y+sys[dir]*d, next_x+sxs[dir]*d
            santa[idx] = [next_y, next_x, 1, point]
            if in_range(next_y, next_x):
                # 연쇄 반응
                push_santa(idx, dir, sys, sxs, 1, ey, ex)
            else:
                lose_santa.add(idx)
        # 아무것도 없다면 그냥 이동
        else:
            santa[idx] = [next_y, next_x, stun, point]
        # print(idx, "번", santa)
    for idx in santa:
        # 탈락이면 패스
        if idx in lose_santa:
            continue
        santa[idx][3]+=1
    # print(k, "턴", santa)
    # print(k, "죽음", lose_santa)


for i in santa:
    print(santa[i][3], end=' ')