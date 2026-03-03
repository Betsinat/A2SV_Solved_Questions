n = int(input())
contest = list(map(int, input().split()))
contest.sort()  
day = 1
for c in contest:
    if c >= day:   
        day += 1   

print(day - 1)