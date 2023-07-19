A = int(input())

for i in range(A):
    R, S = input().split()
    R = int(R)
    S = str(S)
    for i in range(len(S)):
        print(R*S[i], end = '')
    print()
