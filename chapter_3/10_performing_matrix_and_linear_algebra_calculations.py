import numpy as np

if __name__ == "__main__":
    m = np.matrix([[1, -2, 3], [0, 4, 5], [7, 8, -9]])
    print(m)
    print(m.T)
    print(m.I)

    v = np.matrix([[2], [3], [4]])
    print(v)

    print(m*v)

    # 2
    print(np.linalg.det(m))
    print(np.linalg.eigvals(m))

    x = np.linalg.solve(m, v)
    print(x)

    print(m*x)
    print(v)

