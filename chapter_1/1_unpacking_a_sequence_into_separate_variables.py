def run():
    # 1
    p = (4, 5)
    x, y = p
    print(x)
    print(y)

    data = ["ACME", 50, 91.1, (2012, 12, 21)]
    name, shares, price, date = data
    print(name)
    print(shares)
    print(price)
    print(date)

    # 2
    print("------------")
    name, shares, price, (year, month, day) = data
    print(name)
    print(shares)
    print(price)
    print(date)

    print(year)
    print(month)
    print(day)

    # 3
    p = (4, 5)
    # x, y, z = p

    # 4
    s = "Hello"
    a, b, c, d, e = s
    print(a)
    print(c)
    print(d)

    # 5
    data = ["ACME", 50, 91.1, (2012, 12, 21)]
    _, shares, price, _ = data  # 😇
    print('--5--')
    print(shares)
    print(price)


if __name__ == "__main__":
    run()
