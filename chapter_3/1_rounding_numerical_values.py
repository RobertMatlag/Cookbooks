if __name__ == "__main__":
    print(round(1.23, 1))
    print(round(1.27, 1))
    print(round(-1.27, 1))
    print(round(1.25361, 3))

    # 2 równa do najbliższej parzystej
    print(round(1.5))
    print(round(2.5))

    # 3
    a = 1627731
    print(round(a, -1))
    print(round(a, -2))
    print(round(a, -3))

    # 4
    x = 1.23456
    print(format(x, "0.2f"))
    print(format(x, "0.3f"))
    print("value is {:0.3f}".format(x))

    # 5
    a = 2.1
    b = 4.2
    print(a + b) # tutaj nie używać round() żeby ratować sytuacje, tylko uzyć modułu decimal
