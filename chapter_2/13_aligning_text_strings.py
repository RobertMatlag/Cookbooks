text = "Hello world"
if __name__ == "__main__":
    print(text.ljust(20, "-"))
    print(text.rjust(20, "-"))
    print(text.center(20, "-"))

    print(format(text, "-<20"))
    print(format(text, "->20"))
    print(format(text, "-^20"))

    # 2
    print("{:*<10s} {:-<10s}".format("Hello", "world"))

    # 3
    x = 1.23456
    print(format(x, "*^10.2f"))
