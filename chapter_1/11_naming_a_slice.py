record = "....................100.......513.25.........."
if __name__ == "__main__":
    SHARES = slice(20, 23)
    PRICE = slice(30, 36)

    cost = int(record[SHARES]) * float(record[PRICE])

    print(cost)

    a = slice(1, 100, 5)
    print(a.start)
    print(a.stop)
    print(a.step)

    s = 'HelloWorld111wdscddadsa'
    print(a.indices(len(s)))

    for i in range(*a.indices(len(s))):
        print(s[i])

