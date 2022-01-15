import cmath
import math

import numpy as np

if __name__ == "__main__":
    a = complex(2, 4)
    b = 3 - 5j
    print(a)
    print(b)

    print(a.real)
    print(a.imag)

    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
    print(abs(a))

    # 2
    print(cmath.sin(a))
    print(cmath.cos(a))
    print(cmath.exp(a))

    # 3
    a = np.array([2 + 3j, 4 + 5j, 6 - 7j, 8 + 9j])
    print(a)
    print(a + 2)
    print(np.sin(a))

    # 4 math nie ma liczb złożonych
    # print(math.sqrt(-1))
    print(cmath.sqrt(-1))
