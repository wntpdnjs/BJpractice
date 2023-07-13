N, M = map(int, input().split())

basket=[i for i in range(1,N+1)]

for i in range (M) :
    first, second = map(int, input().split())
    basket[first-1:second]=reversed(basket[first-1:second])

for x in basket:
    print(x, end=' ')