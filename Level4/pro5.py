N, M = map(int, input().split())

basket = [0 for _ in range(N)]

for _ in range(M):
    a,b,c = map(int, input(). split())
    for j in range (a,b+1):
        basket[j-1]=c 
    
for j in range(N):
    print(basket[j], end=' ')




