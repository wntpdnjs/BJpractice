correct_num = [1, 1, 2, 2, 2, 8]
found_num = list(map(int, input().split()))

for i in range(6):
    print(correct_num[i]-found_num[i], end=" ")
