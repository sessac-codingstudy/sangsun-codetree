n = int(input())

count =0 
while True:
    if n ==1:
        break
    count += 1
    if n % 2 == 0:
        n //= 2
    elif n % 2 == 1:
        n = n*3 +1
print(count)