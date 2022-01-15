import math

if __name__ == "__main__":
    inf = float("inf")
    minf = float("-inf")
    nan = float("nan")

    print(math.isinf(inf))
    print(math.isinf(minf))
    print(math.isnan(nan))

    # 2
    print(inf + 45)
    print(inf * 10)
    print(10 / inf)

    print(inf / inf)
    print(inf + minf)

    print(nan + 23)
    print(nan / 2)
    print(nan * 2)
    print(math.sqrt(nan))

    # 3 NaN nie można porównywać
    nan2 = float('nan')
    print(nan == nan2)
    print(nan is nan2)
