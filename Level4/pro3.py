A = int(input())
C = list(map(int, input().split()))
B = C[0]

for i in range(A):
    if B>C[i]:
        B=C[i]

D=C[0]
for i in range(A):
    if D<C[i]:
        D=C[i]

print(B, D)
        