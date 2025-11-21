a, b = map(int, input().split())
answer = 0
count = 0
for a in range(a,b+1):
    if a % 5 ==0 or a% 7 ==0:
        answer += a
        count += 1
print(answer, round(answer/count, 1))