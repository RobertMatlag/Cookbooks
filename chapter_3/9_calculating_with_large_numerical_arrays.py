import numpy as np

if __name__ == "__main__":
    x = [1, 2, 3, 4]
    y = [5, 6, 7, 8]

    print(x * 2)
    # print(x + 2)

    ax = np.array(x)
    ay = np.array(y)
    print(ax)
    print(ay)

    print(ax * 2)
    print(ax + 2)
    print(ax + ay)
    print(ax * ay)

    def f(x):
        return 3 * x ** 2 - 2 * x + 7

    print(f(ax))

    # 2
    print(np.sqrt(ax))
    print(np.cos(ax))

    grid = np.zeros(shape=(10000, 10000), dtype=float)
    print(grid)

    grid += 10
    print(grid)

    print(np.sin(grid))

    # 4
    a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    # select row
    print(a[1])
    # select column
    print(a[:, 1])
    a[1:3, 1:3] += 10
    print(a)

    b = a + [100, 101, 102, 103]
    print(b)

    print(np.where(a < 10, a, 10))
