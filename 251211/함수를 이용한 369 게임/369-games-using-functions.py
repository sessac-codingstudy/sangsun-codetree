a, b = map(int, input().split())

# Please write your code here.
def con(i):
    answer = False
    if '3' in str(i) or '6' in str(i) or '9' in  str(i):
        answer = True
    return answer

def sol(a,b):
    count = 0
    for i in range(a,b+1):
        if con(i) or i%3==0:
            count += 1
    return count

print(sol(a,b))

