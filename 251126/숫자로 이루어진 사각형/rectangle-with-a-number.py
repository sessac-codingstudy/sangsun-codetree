n = int(input())

# Please write your code here.
def solution(n):
    count = 1
    for _ in range(n):
        for _ in range(n):
            print(count % 10, end=' ')
            count += 1
            if count == 10:
                count =1 
        print()

solution(n)