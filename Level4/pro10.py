size = int(input())
subject = list(map(int, input().split()))

max_score = max(subject)

for i in range(size):
    subject[i]=subject[i]/max_score*100
print(sum(subject)/size)
    



