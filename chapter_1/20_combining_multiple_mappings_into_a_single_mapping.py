from collections import ChainMap

a = {"x": 1, "z": 3}
b = {"y": 2, "z": 4}

if __name__ == "__main__":
    c = ChainMap(a, b)
    print(c)
    print(c["x"])
    print(c["y"])
    print(c["z"])

    # 2
    values = ChainMap()
    values["x"] = 1
    print(values)
    values = values.new_child()
    print(values)
    values["x"] = 2
    print(values)

    values = values.new_child()
    print(values)
    values["x"] = 3
    print(values)

    values = values.parents
    print(values)
    print(values["x"])

    values = values.parents
    print(values)
    print(values["x"])

    # 3 tworzy kolejny doct i nadpisuje wartosci z dict a przez dict b
    merged = dict(a)
    merged.update(b)
    print(merged)
