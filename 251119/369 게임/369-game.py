n = int(input())
count = 1
while count <= n:
    if count % 3 == 0 or any(c in '369' for c in str(count)):
        print(0, end = ' ')
    else:
        print(count, end = ' ')
    count += 1