n, k, q = map(int, input().split())
temp = [0] * 200002        
admissible = [0] * 200002  
prefix = [0] * 200002     


for _ in range(n):
    l, r = map(int, input().split())
    temp[l] += 1
    temp[r + 1] -= 1

for i in range(1, 200001):
    temp[i] += temp[i - 1]

for i in range(1, 200001):
    if temp[i] >= k:
        admissible[i] = 1

for i in range(1, 200001):
    prefix[i] = prefix[i - 1] + admissible[i]

for _ in range(q):
    a, b = map(int, input().split())
    print(prefix[b] - prefix[a - 1])