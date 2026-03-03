test = int(input())

for _ in range(test):
    casinos, coin = map(int, input().split())
    all_casinos = []
    for _ in range(casinos):
        l, r, real = map(int, input().split())
        all_casinos.append([l, r, real])
    all_casinos.sort()
    current_coins = coin
  
    for i in range(casinos):
        l, r, real = all_casinos[i]
        if l <= current_coins <= r:
            if real > current_coins:
                current_coins = real
    max_final = current_coins
    for i in range(casinos):
        l, r, real = all_casinos[i]
        if l <= current_coins <= r:
            if real > max_final:
                max_final = real
                
    print(max_final)