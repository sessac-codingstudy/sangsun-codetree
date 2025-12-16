a, o, c = input().split()
a = int(a)
c = int(c)

# Please write your code here.
def sol(a,o,c):
    if o == "+":
        print(a,o,c,"=", a+c)
    elif o == "-":
        print(a,o,c,"=", a-c)
    elif o == "/":
        print(a,o,c,"=", a//c)
    elif o == "*":
        print(a,o,c,"=", a*c)
    else:
        print("False")
    
sol(a,o,c)