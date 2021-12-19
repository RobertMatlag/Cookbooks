def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


def dedupe2(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield val
            seen.add(val)


if __name__ == "__main__":
    # 1
    a = [1, 5, 2, 1, 9, 1, 5, 10]
    print(list(dedupe(a)))

    # 2 usuwa duplicaty kiedy powtarza sie x i y
    b = [{"x": 1, "y": 2}, {"x": 1, "y": 3}, {"x": 1, "y": 2}, {"x": 2, "y": 4}]
    print(list(dedupe2(b, key=lambda d: (d["x"], d["y"]))))

    # 3 usuwa duplicaty kiedy powtarza się x
    print(list(dedupe2(b, key=lambda d: d["x"])))
