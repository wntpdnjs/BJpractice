A, B, H = map (int,input().split())

ground = 0
cnt = -1

cnt = (H-B) / (A-B)
if cnt == int(cnt) :
    print(int(cnt))
else:
    print(int(cnt)+1)



