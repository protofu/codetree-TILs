l, n, q = tuple(map(int, input().split()))

chess = [[2]*(l+2)]
for _ in range(l):
    chess.append([2]+list(map(int, input().split()))+[2])
chess.append([2]*(l+2))

heal = [0]*(n+1)
knight = {}
for i in range(1, n+1):
    r, c, h, w, k = tuple(map(int, input().split()))
    knight[i] = [r, c, h, w, k]
    heal[i] = k


command = []
for _ in range(q):
    i, d = tuple(map(int, input().split()))
    command.append((i, d))
# 1위 2오 3아 4왼
dys, dxs = [-1, 0, 1, 0], [0, 1, 0, -1]
damage = []

def in_range(y, x):
    return 0<y and y<=l and 0<x and x<=l

def push_knight(start, dr):     # start를 밀고, 연쇄처리
    q = []                      # push 후보 저장
    pset = set()                # 이동 기사번호 저장
    damage = [0]*(n+1)
    q.append(start)             # 초기 데이터 append
    pset.add(start)

    while q:
        cur = q.pop(0)          # 기사 번호
        cr, cc, h, w, k = knight[cur]

        # 명령받은 방향진행, 벽이 아니면, 겹치는 다른 기사 => q에 append
        nr, nc = cr+dys[dr], cc+dxs[dr]
        for i in range(nr, nr+h):
            for j in range(nc, nc+w):
                if chess[i][j]==2:      # 벽이라면?
                    return
                if chess[i][j]==1:      # 함정이라면
                    damage[cur]+=1
        # 겹치는 기사 있는 경우 q에 append
        for idx in knight:
            if idx in pset:             # 이미 겹쳐있던 대상이면
                continue
            tr, tc, th, tw, _ = knight[idx]

            if nr<=tr+th-1 and nr+h-1>=tr and nc<=tc+tw-1 and nc+w-1>=tc:
                q.append(idx)
                pset.add(idx)

    # 명령 기사는 데미지 없음
    damage[start] = 0
    # 나머지 이동처리, 체력 0 이하면 삭제
    for idx in pset:
        sr, sc, h, w, k = knight[idx]

        if k <= damage[idx]:
            knight.pop(idx)
        else:
            nr, nc = sr+dys[d], sc+dxs[d]
            knight[idx] = [nr, nc, h, w, k-damage[idx]]


for cmd in command:
    i, d = cmd
    # 해당 기사가 없다면 패스
    if i in knight:
        push_knight(i, d)

ans = 0
for idx in knight:
    ans += heal[idx]-knight[idx][4]
print(ans)