l, n, q = map(int ,input().split())

chess = [[2]*(l+2)] + [[2]+list(map(int, input().split()))+[2] for _ in range(l)] + [[2]*(l+2)]
# for i in chess:
#     print(i)
health = [0]*(n+1)
knight = {}
for i in range(1,n+1):
    r, c, h, w, k = map(int, input().split())
    knight[i] = [r, c, h, w, k]
    health[i] = k

command = [list(map(int, input().split())) for _ in range(q)]
# 1위 2오 3아 4왼
dys, dxs = [-1, 0, 1, 0], [0, 1, 0, -1]

ans = 0

def push_chess(start, dr):
    q = []
    qset=set()
    damage = [0] * (n + 1)
    q.append(start)
    qset.add(start)

    while q:
        cur = q.pop(0)
        cr, cc, h, w, k = knight[cur]
        nr, nc = cr+dys[dr], cc+dxs[dr]
        for y in range(nr, nr+h):
            for x in range(nc, nc+w):
                if chess[y][x]==2:
                    return
                if chess[y][x]==1:
                    damage[cur] += 1

        for idx in knight:
            if idx in qset:
                continue
            er, ec, eh, ew, _ = knight[idx]

            if nr<=er+eh-1 and nc<=ec+ew-1 and nc+w-1>=er and nr+h-1>=ec:
                q.append(idx)
                qset.add(idx)
    damage[cur] = 0
    for i in qset:
        sr, sc, h, w, k = knight[i]
        if damage[i] >= k:
            knight.pop(i)
        else:
            nr, nc = sr+dys[dr], sc+dxs[dr]
            knight[i] = [nr, nc, h, w, k-damage[i]]


for com in command:
    idx, dr = com
    if idx in knight:
        push_chess(idx, dr)

for i in knight:
    ans+=health[i]-knight[i][4]
print(ans)