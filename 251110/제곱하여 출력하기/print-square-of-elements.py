N = int(input())
n = list(map(int, input().split()))

for i in range(N):
    print(n[i]**2, end = ' ')