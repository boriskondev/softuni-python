def loading_bar(n):
    if 0 <= n < 100:
        percentages = "%" * int(n / 10)
        dots = "." * int(10 - n / 10)
        print(f"{n}% [{percentages + dots}]")
        print("Still loading...")
    elif n == 100:
        percentages = "%" * int(n / 10)
        print(f"{n}% Complete!")
        print(f"[{percentages}]")


status = int(input())
loading_bar(status)