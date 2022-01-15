import os

if __name__ == "__main__":
    x = 1234
    print(bin(x))
    print(oct(x))
    print(hex(x))

    print(format(x, "b"))
    print(format(x, "o"))
    print(format(x, "x"))

    print(format(-x, "b"))
    print(format(-x, "o"))
    print(format(-x, "x"))

    # unsigned value
    print(format(2 ** 32 + -x, "b"))
    print(format(2 ** 32 + -x, "o"))
    print(format(2 ** 32 + -x, "x"))

    print(int("4d2", 16))
    print(int("10011010010", 2))

    # 2
    os.chmod("4_working_with_binary_octal_and_hexadecimal_integers.py", 0o0664)
