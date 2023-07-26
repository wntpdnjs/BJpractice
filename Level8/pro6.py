A = int(input())

line =0
end=0

while A>end:
    line +=1
    end +=line

diff = end - A 
if line%2 ==0:
    top = line - diff
    bottom = diff+1
else :
    top = diff +1
    bottom = line - diff

print("%d/%d" %(top, bottom))
