A = list(map(int, input().split()))
B = list(map(int, input().split()))

if A[0] == B[0]:
    if A[1] > B[1]:
        print("A")
    else:
        print("B")
elif A[0] > B[0]:
    print("A")
else:
    print("B")