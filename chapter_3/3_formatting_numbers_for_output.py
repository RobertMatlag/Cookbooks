if __name__ == "__main__":
    x = 1234.56789
    print(format(x, "0.2f"))
    print(format(x, ">10.1f"))
    print(format(x, "<10.1f"))
    print(format(x, "^10.1f"))
    print(format(x, ","))
    print(format(x, "0,.1f"))
    print(format(x, "e"))
    print(format(x, "0.2E"))
    # [<>^]?width[,]?(.digits)?  width, digit ->integers

    print("The value is {:0,.2f}".format(x))

    # 2
    print(format(x, "0.1f"))
    print(format(-x, "0.1f"))

    # 3
    swap_separators = {ord("."): ",", ord(","): "."}
    print(format(x, ',.3f').translate(swap_separators))
