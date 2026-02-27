n = int(input())
arr = list(map(int, input().split()))
arr.sort()
median = arr[n // 2]
x = arr[(n-1) //2]
print(x)
