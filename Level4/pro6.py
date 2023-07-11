N, M = map(int, input().split())
basket = [i for i in range(1,N+1)]
for _ in range(M):
    A,B = map(int, input().split())
    X=basket[A-1]
    basket[A-1]=basket[B-1]
    basket[B-1]=X

for X in basket:
    print(X, end=' ')
    
