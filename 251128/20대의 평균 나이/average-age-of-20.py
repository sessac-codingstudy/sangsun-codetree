answer = 0
count = 0
while True:
    n = int(input())
    if n>29 or n < 20:
        break
    count += 1
    answer += n

print(f"{answer/count:.2f}")