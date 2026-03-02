t = int(input())
for _ in range(t):
    n, x, k = map(int, input().split())
    s = input().strip()
    pos = 0
    pref = []
    for ch in s:
        pos += -1 if ch == 'L' else 1
        pref.append(pos)
    t0 = -1
    for i in range(n):
        if x + pref[i] == 0:
            t0 = i + 1
            break
    if t0 == -1 or t0 > k:
        print (0)
        continue
    cycle = -1
    for i in range(n):
        if pref[i] == 0:
            cycle = i + 1
            break
    ans = 1
    if cycle != -1:
        ans += (k -t0) // cycle
    print(ans)
    
