a = input()

fruits = ['apple', 'banana', 'grape', 'blueberry', 'orange']
answer = []
count = 0
for eng in fruits:
    if a == eng[2] or a == eng[3]:
        count += 1
        print(eng)

print(count)

