A = int(input())


for i in range(1,A):
    print(" "*(A-i)+"*"*(1+2*(i-1)))
for i in range(A,0,-1):
    print(" "*(A-i)+"*"*(2*i-1))