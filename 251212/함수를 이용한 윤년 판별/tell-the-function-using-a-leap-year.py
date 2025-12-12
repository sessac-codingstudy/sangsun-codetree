y = int(input())

# Please write your code here.
def is_leap_year(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

print(str(is_leap_year(y)).lower())
