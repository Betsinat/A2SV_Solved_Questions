n , k = map(int , input().split())
arr = list(map(int , input().split()))
gap = []
for i in range(n):
    gap.append(arr[i] - arr[i-1]) 
gap.sort(reverse=True)
ncost = arr[-1] - arr[0]
for i in range(k-1):
    ncost -= gap[i]
print(ncost)