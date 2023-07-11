A, B = map(int, input().split())
C = list(map(int, input().split()))
for i in range(A):
    if C[i]<B:
        print(C[i], end=" ")