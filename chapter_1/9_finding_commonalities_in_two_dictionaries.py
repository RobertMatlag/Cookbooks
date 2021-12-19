a = {"x": 1, "y": 2, "z": 3}

b = {"w": 10, "x": 11, "y": 2}

if __name__ == "__main__":
    # common keys
    print(a.keys() & b.keys())
    # b not in a
    print(a.keys() - b.keys())
    # common key, value pair
    print(a.items() & b.items())

    c = {key: a[key] for key in a.keys() - {"z", "w"}}
    print(c)
