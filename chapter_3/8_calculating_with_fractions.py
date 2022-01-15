from fractions import Fraction

if __name__ == "__main__":
    a = Fraction(5, 4)
    b = Fraction(7, 16)

    print(a + b)
    print(a * b)
    c = a * b
    print(c.numerator)
    print(c.denominator)

    # 2
    print(float(c))
    print(c.denominator)
    print(c.limit_denominator(63))

    # 3
    x = 3.75
    print(x.as_integer_ratio())
    print(Fraction(*x.as_integer_ratio()))


