import math
from decimal import Decimal, localcontext

if __name__ == "__main__":
    a = 4.2
    b = 2.1
    print(a + b)
    print((a + b) == 6.3)

    # 2
    a = Decimal("4.2")
    b = Decimal("2.1")

    print(a + b)
    print((a + b) == Decimal("6.3"))

    # 3
    a = Decimal("1.3")
    b = Decimal("1.7")

    print(a / b)

    with localcontext() as ctx:
        ctx.prec = 3
        print(a / b)

    with localcontext() as ctx:
        ctx.prec = 50
        print(a / b)

    # 4
    nums = [1.23e18, 1, -1.23e18]
    print(sum(nums)) # 1 disappaers

    print(math.fsum(nums))

