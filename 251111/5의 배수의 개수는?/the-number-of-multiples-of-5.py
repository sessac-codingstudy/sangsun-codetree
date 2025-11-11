count = 0

for i in range(4):
    answer = []
    answer = list(map(int, input().split()))
    for i in range(4):
        if answer[i] % 5 ==0:
            count += 1
print(count)
    