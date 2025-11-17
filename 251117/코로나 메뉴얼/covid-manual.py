a = list(map(str,input().split()))
b = list(map(str,input().split()))
c = list(map(str,input().split()))
count = 0

if a[0]=='Y' and int(a[1]) >=37:
    count +=1
if b[0]=='Y' and int(b[1]) >=37:
    count +=1
if c[0]=='Y' and int(c[1]) >=37:
    count +=1

if count >= 2:
    print("E")
else:
    print("N")
