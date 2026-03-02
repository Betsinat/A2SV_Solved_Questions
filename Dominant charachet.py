t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    ans = float('inf')
    
    for i in range(n - 1):  
        if s[i] == 'a' and s[i+1] == 'a':
            ans = min(ans, 2)
    
    for i in range(n - 2):  
        sub = s[i:i+3]
        if sub.count('a') > sub.count('b') and sub.count('a') > sub.count('c'):
            ans = min(ans, 3)
    
    for i in range(n - 3):  
        sub = s[i:i+4]
        if sub.count('a') > sub.count('b') and sub.count('a') > sub.count('c'):
            ans = min(ans, 4)
    
    for i in range(n - 6):  
        sub = s[i:i+7]
        if sub.count('a') > sub.count('b') and sub.count('a') > sub.count('c'):
            ans = min(ans, 7)
    
    print(-1 if ans == float('inf') else ans)
            
