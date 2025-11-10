N, M = map(int, input().split())
a_matrix = []
b_matrix = []
for i in range(N):
    a_matrix.append(list(map(int, input().split())))
for i in range(N):
    b_matrix.append(list(map(int, input().split())))

answer = []
for i in range(N):
    for j in range(M):
        if a_matrix[i][j] == b_matrix[i][j]:
            print(0, end = ' ')
        else:
            print(1, end = ' ')
    print()