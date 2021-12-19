nums = [1, 2, 3, 4, 5]
if __name__ == "__main__":
    s = sum(x * x for x in nums)
    print(s)

    # 2

    import os

    files = os.listdir(".")
    if any(name.endswith(".py") for name in files):
        print("There be python!")
    else:
        print("Sorry, no python.")

    # 3

    s = ("ACME", 50, 123.45)
    print(",".join(str(x) for x in s))

    # 4
    portfolio = [
        {"name": "GOOG", "shares": 50},
        {"name": "YHOO", "shares": 75},
        {"name": "AOL", "shares": 20},
        {"name": "SCOX", "shares": 65},
    ]

    print(min(rec['shares'] for rec in portfolio))


