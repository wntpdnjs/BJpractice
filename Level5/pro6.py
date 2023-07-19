A = list(input())
alpa = 'abcdefghijklmnopqrstuvwxyz'

for i in alpa :
    if i in A : 
        print (A.index(i), end=' ')
    else : 
        print(-1, end=' ')



