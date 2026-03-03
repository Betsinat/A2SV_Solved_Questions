t = int(input().strip())
for _ in range(t):
    n= int(input().strip())
    arr = list(map(int, input().strip().split()))
    subseq=[arr[0]]
    for i in range(1 , n-1):
        if (arr[i] - arr[i-1]) * (arr[i+1]- arr[i])< 0:
            subseq.append(arr[i])
    subseq.append(arr[-1])
    print(len(subseq))
    print(*subseq)