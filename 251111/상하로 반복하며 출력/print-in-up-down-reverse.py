N = int(input())
for i in range(1, N+1):
    answer = ''
    for j in range(1, N+1):
        if j % 2 != 0:
            value = i
        else:
            value = N-i+1
        answer += str(value)
    print(answer)
