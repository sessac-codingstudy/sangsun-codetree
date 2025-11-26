while True:
    user = int(input())
    if user < 25:
        print("Higher")
    elif user > 25:
        print("Lower")
    elif user == 25:
        print("Good")
        break